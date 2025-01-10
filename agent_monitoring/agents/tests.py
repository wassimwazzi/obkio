import unittest.mock
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Agent
import unittest
import datetime


class AgentApiTests(APITestCase):

    def test_create_agent(self):
        data = {"ip_address": "192.168.1.5"}

        response = self.client.post("/api/agents/", data, format="json")
        agent_id = response.data["id"]

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        agent = Agent.objects.get(id=agent_id)
        self.assertIsInstance(agent.last_reported, datetime.datetime)

    @unittest.mock.patch("agents.views.get_ip_info")
    def test_auto_sets_asn_and_ip(self, mock_get_ip_info):
        mock_asn, mock_isp = "AS1234", "Test ISP"
        mock_get_ip_info.return_value = (mock_asn, mock_isp)
        data = {"ip_address": "192.168.1.5"}

        response = self.client.post("/api/agents/", data, format="json")
        self.assertEqual(response.data["asn"], mock_asn)
        self.assertEqual(response.data["isp"], mock_isp)

    def test_cannot_manually_set_asn_and_ip(self):
        data = {"ip_address": "192.168.1.5", "asn": "test_asn", "isp": "test_isp"}

        response = self.client.post("/api/agents/", data, format="json")
        agent_id = response.data["id"]

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        agent = Agent.objects.get(id=agent_id)
        self.assertIsNone(agent.isp)
        self.assertIsNone(agent.asn)

    def test_get_agent(self):
        agent = Agent.objects.create(ip_address="192.168.1.6")

        response = self.client.get(f"/api/agents/{agent.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ip_address"], agent.ip_address)
        self.assertEqual(response.data["asn"], agent.asn)
        self.assertEqual(response.data["isp"], agent.isp)

    def test_update_agent(self):
        agent = Agent.objects.create(ip_address="192.168.1.7")

        new_ip = "192.168.1.6"
        updated_data = {
            "ip_address": new_ip,
        }
        prev_timestamp = agent.last_reported

        response = self.client.put(
            f"/api/agents/{agent.id}/", updated_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        agent.refresh_from_db()
        self.assertEqual(agent.ip_address, new_ip)
        self.assertGreater(agent.last_reported, prev_timestamp)

import asyncio
import logging

import httpx

from settings.config import MAIN_URL

logger = logging.getLogger(__name__)


class SmsHubAPI:
    """
    SmsHubAPI class for interacting with the SmsHub API.
    """

    def __init__(self):
        """
        Initialize the SmsHubAPI class.
        """
        self.main_url = MAIN_URL

    async def get_balance(self):
        """
        Get balance from smshub.org

        :return: string: balance available on the smshub account
        """
        url = f'{self.main_url}getBalance'
        try:
            response = await httpx.AsyncClient().get(url)
            logger.info(f'Balance requested: {response.text}')
            return response.text[15:]
        except Exception as e:
            logger.error(e)
            return e

    async def get_number(self, service, country=6):
        """
        Get phone number from smshub.org for the specified service and country.

        :param service: string: service for which the number is needed
        :param country: int (optional): country code for the required
        phone number, defaults to 0 (any)
        :return: tuple: phone number and its id, or error message
        in case of issues
        """
        url = f'{self.main_url}getNumber&service={service}&country={country}'
        try:
            response = await httpx.AsyncClient().get(url)
            logger.info(f'Number requested: {response.text}')
            if response.text == 'NO_NUMBERS':
                return 'Numbers are over'
            elif response.text == 'NO_BALANCE':
                return 'Not enough money'
            number_id = response.text[14:23]
            number = response.text[24:38]
            return number, number_id
        except Exception as e:
            logger.error(e)
            return e

    async def request_status(self, number_id):
        """
        Request status of a phone number from smshub.org

        :param number_id: string: id of the phone number
        :return: string: status of the phone number
        """
        url = f'{self.main_url}getStatus&id={number_id}'
        try:
            response = await httpx.AsyncClient().get(url)
            logger.info(f'Status requested:{number_id} - {response.text}')
            return response.text
        except Exception as e:
            logger.error(e)
            return e

    async def check_status(self, number_id):
        """
        Continuously check the status of a phone number on smshub.org

        :param number_id: string: id of the phone number
        :return: string: final status of the phone number or error message
        """
        try:
            for check in range(600):
                status = await self.request_status(number_id)
                logger.info(f'Checking status: {status}')
                await asyncio.sleep(5)
                if status == 'STATUS_WAIT_CODE':
                    continue
                elif status.split(':')[0] == 'STATUS_OK':
                    return status[10:]
                elif status == 'STATUS_CANCEL':
                    return 'Number closed'
        except Exception as e:
            logger.error(e)
            return e

    async def set_status(self, number_id, status):
        """
        Set status for a phone number on smshub.org

        :param number_id: string: id of the phone number
        :param status: int: new status to be set for the phone number
        :return: string: response from the API or error message
        """
        url = f'{self.main_url}setStatus&status={status}&id={number_id}'
        try:
            response = await httpx.AsyncClient().get(url)
            logger.info(f'Status set: {response.text}')
            return response.text
        except Exception as e:
            logger.error(e)
            return e

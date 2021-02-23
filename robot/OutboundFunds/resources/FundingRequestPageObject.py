from cumulusci.robotframework.pageobjects import ListingPage
from cumulusci.robotframework.pageobjects import DetailPage
from cumulusci.robotframework.pageobjects import pageobject
from BaseObjects import BaseOutboundFundsPage


@pageobject("Listing", "Funding_Request__c")
class FundingRequestListingPage(BaseOutboundFundsPage, ListingPage):

    def _is_current_page(self):
        """Verify we are on the Funding Request Listing page
        by verifying that the url contains '/view'
        """
        self.selenium.location_should_contain(
            "Funding_Request__c/list?",
            message="Current page is not a Funding Request List view",
        )


@pageobject("Details", "Funding_Request__c")
class FundingRequestDetailPage(BaseOutboundFundsPage, DetailPage):

    def _is_current_page(self):
        """Verify we are on the Funding Request detail page
        by verifying that the url contains '/view'
        """
        self.selenium.wait_until_location_contains(
            "/view", timeout=60, message="Detail page did not load in 1 min"
        )

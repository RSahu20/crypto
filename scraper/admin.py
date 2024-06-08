from django.contrib import admin
from .models import Job, Scrapping_Details, Contracts, Official_Links, Socials

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_id']
    # Add any other configuration options as needed

@admin.register(Scrapping_Details)
class ScrappingDetailsAdmin(admin.ModelAdmin):
    list_display = [ 'coin', 'price', 'price_change', 'market_cap', 'market_cap_rank', 'volume', 'volume_rank', 'volume_change', 'circulating_supply', 'total_supply', 'diluted_market_cap']
    # Add any other configuration options as needed

@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    list_display = ['scraping_details', 'name', 'address']
    # Add any other configuration options as needed

@admin.register(Official_Links)
class OfficialLinksAdmin(admin.ModelAdmin):
    list_display = ['scraping_details', 'name', 'link']
    # Add any other configuration options as needed

@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ['scraping_details', 'name', 'link']
    # Add any other configuration options as needed

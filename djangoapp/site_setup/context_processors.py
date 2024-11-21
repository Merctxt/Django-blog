from site_setup.models import SiteSetup

def Site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return {
        'Site_setup': setup
    }
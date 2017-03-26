import requests

def get_names(url):
	result = requests.get(url)

	if result.status_code == 200:
		return result.json()
	else:
		return False

if __name__ == '__main__':
	print(get_names('https://apidata.mos.ru/v1/datasets/2009/rows')) 
import gdown


class Downloader:
	def __init__(self, input_url, output_name):
		self.input_url = input_url
		self.output_name = output_name

	def download_from_gdrive(self):
		gdown.download(self.input_url, self.output_name, quiet=False)



#url = 'https://drive.google.com/uc?id=15Xfy-uf1d3SmtK7b5oTGKuCFfap3Anuv'
#output = 'renewable_power_plants_DE.csv'
#gdown.download(url, output, quiet=False)

#md5 = '567703f6a41ee9a9587862053c63fe7e'
#gdown.cached_download(url, output, md5=None, postprocess=gdown.extractall)

#orig_url='https://drive.google.com/file/d/15Xfy-uf1d3SmtK7b5oTGKuCFfap3Anuv/view?usp=sharing'

#file_id = orig_url.split('/')[-2]
#print(file_id)
#dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
#url = requests.get(dwn_url).text
#csv_raw = StringIO(url)
#dfs = pd.read_csv(csv_raw)
#print(dfs.head())
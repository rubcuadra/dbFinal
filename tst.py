api_key = '95172a7324019870220fd4304684e07d'  
from paybook.sdk import Paybook  
pb = Paybook(api_key,db_environment=True,logger=None)

r = pb.signup("sdk_test","pass")
print r  

r = pb.login("sdk_test","pass")
print r  

token=r["token"]
print token

r = pb.catalogues(token=token)  
for site in r:  
	if site['name'] == 'SAT':  
		id_site = site['id_site']
		print id_site

credentials = {'rfc':'SAGS5404299V9', 'password':'adriana1'}

credentials_response = pb.credentials(token=token, id_site=id_site, credentials=credentials)
print credentials_response

status_response = pb.status(token=token, id_site=id_site, url_status=credentials_response['status']) 
print status_response 
for c in status_response:
	if c['code'] == 202 or c['code'] == 200:
		print 'True'

transactions_response= pb.transactions(token=token, id_account=None)
print transactions_response
for tr in transactions_response:
	print tr
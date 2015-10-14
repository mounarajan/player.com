import urllib.request
import os
import re
import time
import sys
import csv
import time

class Libraries(object):
	#Some websites will keep blocking or will throw different page than live url so we can use any of this function to bypass the blockages
	while True:
		try:

			def wget(self,url):
				self.data = os.popen('wget -qO- %s'% url).read()
				return self.data

			def wget_cookie(self,url):
				self.data = os.popen('wget -qO- --no-cookies --header "Cookie: zipcode=N0P2J0" %s'% url).read()
				return self.data

			def wget_sepcial(self,url):
				self.data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
				return self.data

			def curl(self,url):

				self.url = url 
				self.data = os.popen('curl --silent --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" %s >/dev/null'% self.url).read()
				return self.data

			def curl_special(self,url):

				self.url = url 
				self.data = os.popen('curl -O %s >/dev/null'% self.url).read()
				return self.data

			def urllib(self,url):
				filename = "cookies.txt"
				self.url = url 
				headers = {}
				headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
				req = urllib.request.Request(url, headers = headers)
				resp = urllib.request.urlopen(req)
				self.data = resp.read()

		except:
			continue
			time.sleep(3)
		break

class Out(Libraries):
	#This function will extract a to z pages 

	def links_extract(self,url):
		f2 = open('main-urls.txt','w')
		url = re.sub(r"[\s\n]*","",url)
		#url = re.sub(r'\&','\&',url)
		output.urllib(url)
		data = self.data 
		data = str(data)
		#print (data)

		if re.search(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data):
			links = re.findall(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data)
			for link in links:
				if re.search(r'^htt',link):
					f2.write(link+"\n")
					print (link+"\n")
				elif re.search(r'\w',link):
					link = re.sub(r'^','http://youtube.com/channel/',link)
					link = re.sub(r'(.*?channel\/.*)',r'\1/about',link)
					link = re.sub(r'amp\;',r'',link)
					f2.write(link+"\n")
					print (link+"\n")
					output.data_extract(link)
		if re.search(r'(?mis)&pageToken=\w+',url):
			url = re.sub(r'&pageToken=\w+',r'',url)
		if re.search(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data):
			links = re.findall(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data)[0]
			url = url+"&pageToken={0}".format(links)
			print (url)
			output.links_extract(url)

	def data_extract(self,url):
		f1 = open('presonal_urls.txt','a')
		f2 = open('facebook_urls.txt','a')
		f3 = open('crawled_email1','a')
		url = re.sub(r"[\s\n]*","",url)
		url = re.sub(r'\&','\&',url)
		output.wget_sepcial(url)
		data = self.data 
		data = str(data)

		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
			if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
				email = re.sub(r'(.*)\/',r"\1",email)
				f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
				print (email)							

		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
			for mail in email:
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
					mail = re.sub(r'(.*)\/',r"\1",mail)
					f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
					print (mail)
		if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
			must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
			for mail in must:
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
					mail = re.sub(r'(.*)\/',r"\1",mail)
					f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
					print (mail)

		if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
			ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
			ear = re.sub(r'(.*)\/',r"\1",ear)
			f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
			print (ear)

		if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
			ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
			for mail in ear:
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
					mail = re.sub(r'(.*)\/',r"\1",mail)
					f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
					print (mail) 

		if re.search(r'(?mis)<a\shref\=\"([^\"]*\.com)\"\srel\=\"me.*?title\=\"[^\"]*\"',data):
			email = re.findall(r'(?mis)<a\shref\=\"([^\"]*\.com)\"\srel\=\"me.*?title\=\"[^\"]*\"',data)[0]
			print (email)
			f1.write(email)
			output.crawl_fb_again(email) 

		if re.search(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me.*?title\=\"[^\"]*\"',data):
			email = re.findall(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me.*?title\=\"[^\"]*\"',data)[0]
			print (email)
			f1.write(email)
			output.crawl_fb_again(email) 

		if re.search(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me\snofollow\"[^\"]*\"[^\"]*\"\stitle\=\"[^\"]*Facebook\"',data):
			email = re.findall(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me\snofollow\"[^\"]*\"[^\"]*\"\stitle\=\"[^\"]*Facebook\"',data)[0]
			print (email) 
			f2.write(email)
			output.crawl_fb_onceagain(email)


	def dedup_one(self):
		with open('a-to-z-links.txt') as result:
			uniqlines = set(result.readlines())
			with open('a-to-z-links.txt', 'w') as rmdup:
				rmdup.writelines(set(uniqlines))

	def crawl_fb_onceagain(self,url):
		#f1 = open('facebook_crawled_urls','r+')
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled_email_ids_report.json','a')
		if re.search(r'^htt',url):
			lin = re.sub(r"\s*","",url)
			#print (lin)
			try:
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data)
				#print (data)

				if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
					email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
					for fb in email:
						url = re.sub(r'\?.*','',fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							print (fb_cac)
							time.sleep(sleep)
							if re.search(r'^htt',fb_cac):
								#print (lin)
								first = "/info?tab=page_info"
								second = "/about?section=contact-info"
								url = fb_cac+first   
								print (url)  
								try:                                                                                             
									output.wget_sepcial(url)
									data = self.data 
									data = str(data)
									if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
										link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
										for mail in link:
											mail = re.sub(r'\&\#064\;','@',mail)
											f4.write(mail+"\n")
											fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
											for smail in fmail:

												f3.write(smail+"\n")
												f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
												print (smail)
								except Exception: 
									pass    

									#else:
									 #   url = fb_cac+second  
									  #  print (url)
									   # try:                                                                                               
										#    output.wget_sepcial(url)
										 #   data = self.data 
										  #  data = str(data)
										   # if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
											#    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
											 #   for mail in link:
											  #      mail = re.sub(r'\&\#064\;','@',mail)
											   #     f4.write(mail+"\n")
												#    fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
												 #   for smail in fmail:

												  #      f3.write(smail+"\n")
												   #     f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
													#    print (smail)
										#except Exception: 
										 #   pass    

				else: 
					print ("not found")
					f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
			except Exception: 
				pass

	def crawl_fb_again(self,url):
		#f1 = open('facebook_crawled_urls','r+')
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled_email_ids_report.json','a')
		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			#print (lin)
			try:
				url_lin = re.sub(r'(.*?\/)',r"\1",lin)
				print (url_lin)
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data)
				#print (data)
				#print (data)

				if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
					email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
					for fb in email:
						url = re.sub(r'\?.*','',fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							print (fb_cac)
							time.sleep(sleep)
							if re.search(r'^\w',fb_cac):
								try:                                                                                             
									output.wget_sepcial(url)
									data = self.data 
									data = str(data)
									#print (data)
									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
										if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
											email = re.sub(r'(.*)\/',r"\1",email)
											f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
											print (email)

									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
										for mail in email:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)
									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
										for mail in must:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)

									if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
										ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
										ear = re.sub(r'(.*)\/',r"\1",ear)
										f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
										print (ear)

									if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
										ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
										for mail in ear:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)

									if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										if re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										
										print (ear)
										output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
										if re.search(r'(?mis)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										if re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
									
										print (ear[0])
										output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										if re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
									
										print (ear)
										output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
										if re.search(r'(?mis)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										if re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										
										print (ear[0])
										output.link_again(ear[0],sleep)

								except Exception: 
									pass    

									#else:
									 #   url = fb_cac+second  
									  #  print (url)
									   # try:                                                                                               
										#    output.wget_sepcial(url)
										 #   data = self.data 
										  #  data = str(data)
										   # if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
											#    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
											 #   for mail in link:
											  #      mail = re.sub(r'\&\#064\;','@',mail)
											   #     f4.write(mail+"\n")
												#    fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
												 #   for smail in fmail:

												  #      f3.write(smail+"\n")
												   #     f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
													#    print (smail)
										#except Exception: 
										 #   pass    

				else: 
					print ("not found")
					f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
			except Exception: 
				pass  

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			#print (lin)
			try:
				url_lin = re.sub(r'(.*?\/)',r"\1",lin)
				#print (url_lin)
				output.urllib(lin)
				data = self.data 
				data = str(data)
				#print (data)
				#print (data)

				if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
					email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
					for fb in email:
						url = re.sub(r'\?.*','',fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							print (fb_cac)
							time.sleep(sleep)
							if re.search(r'^\w',fb_cac):
								try:                                                                                             
									output.wget_sepcial(url)
									data = self.data 
									data = str(data)
									#print (data)
									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
										if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
											email = re.sub(r'(.*)\/',r"\1",email)
											f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
											print (email)

									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
										for mail in email:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)
									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
										for mail in must:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)

									if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
										ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
										ear = re.sub(r'(.*)\/',r"\1",ear)
										f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
										print (ear)

									if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
										ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
										for mail in ear:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)

									if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										elif re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										else:
											print (ear)
											output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										elif re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										else:
											print (ear[0])
											output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a.*?href\=\"([^\"]*\/contact.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*\/contact.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										if re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										
										print (ear)
										output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										if re.search(r'(?mis)^.*',ear[0]):
											ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										
										print (ear[0])
										output.link_again(ear[0],sleep)

								except Exception: 
									pass    

									#else:
									 #   url = fb_cac+second  
									  #  print (url)
									   # try:                                                                                               
										#    output.wget_sepcial(url)
										 #   data = self.data 
										  #  data = str(data)
										   # if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
											#    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
											 #   for mail in link:
											  #      mail = re.sub(r'\&\#064\;','@',mail)
											   #     f4.write(mail+"\n")
												#    fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
												 #   for smail in fmail:

												  #      f3.write(smail+"\n")
												   #     f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
													#    print (smail)
										#except Exception: 
										 #   pass    

				else: 
					print ("not found")
					f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
			except Exception: 
				pass    

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				url_lin = re.sub(r'(.*?\/)',r"\1",lin)
				#print (url_lin)
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data) 
				
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")

				if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
					print ("yes")
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
					#print (ear)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
					print ("yes")
					ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
					#print (ear)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

			except Exception: 
				pass  

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				url_lin = re.sub(r'(.*?\/)',r"\1",lin)
				#print (url_lin)
				output.urllib(lin)
				data = self.data 
				data = str(data) 

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")

				if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
					print ("yes")
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
					#print (ear)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data):
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
					print ("yes")
					ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
					#print (ear)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)

					print (ear)
					output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a.*?href\=\"([^\"]*\/about.*?[^\"]*)\"',data):
					ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*\/about.*?[^\"]*)\"',data)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					if re.search(r'(?mis)^.*',ear[0]):
						ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					
					print (ear)
					output.link_again(ear[0],sleep)

			except Exception: 
				pass  

	def link_again(self,url,sleep):
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled_email_ids_report.json','a')
		f6 = open('contact-links','a')

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			try:
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data) 

				if re.search(r'(?mis)\"textarea',data):
					print ("This is contact")
					f6.write(lin+"\n")
				if re.search(r'(?mis)form\"',data):
					print ("This is contact")
					f6.write(lin+"\n")
				if re.search(r'(?mis)\"form',data):
					print ("This is contact")
					f6.write(lin+"\n")
				if re.search(r'(?mis)\"submit',data):
					print ("This is contact")
					f6.write(lin+"\n")
			except Exception: 
				pass  

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			try:
				output.urllib(lin)
				data = self.data 
				data = str(data) 

				if re.search(r'(?mis)\"textarea',data):
					print ("This is contact")
					f6.write(lin+"\n")
				if re.search(r'(?mis)form\"',data):
					print ("This is contact")
					f6.write(lin+"\n")
				if re.search(r'(?mis)\"form',data):
					print ("This is contact")
					f6.write(lin+"\n")
				if re.search(r'(?mis)\"submit',data):
					print ("This is contact")
					f6.write(lin+"\n")
			except Exception: 
				pass 
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data) 

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")

			except Exception: 
				pass  

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				output.urllib(lin)
				data = self.data 
				data = str(data) 

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")

			except Exception: 
				pass


	def main_data_to_csv(self):
		#This page will extract data what we need
		data_store = []
		
		#data_store = hh
		f2 = open('main-urls.txt','r')
		f3 = open("test_data.csv", 'wt')
		f4 = open("urls.csv", 'wt')
		writer = csv.writer(f3)
		writer.writerow( ('Name', 'URL', 'Acronym','Website','Main Address','Phone Number','Contact','Parent Name','Parent URL','Parent Acronym','Parent Website','Parent Main Address','Parent Phone Number','Parent Contact') )
		for link in f2:
			
			link = re.sub(r"[\s\n]*","",link)
			link = re.sub(r'\&','\&',link)
			print (link)
			try:
				output.wget_sepcial(link)
				data = self.data 
				data = str(data)
			except:
				pass

			if re.search(r'(?mis)companyName\">([^<]*)',data):
				name = re.findall(r'(?mis)companyName\">([^<]*)',data)[0]
				#name = re.sub(r'[\,\.]*','',name)
				#print (name)
				ss = name																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
				data_store.append("{\"name\":\"%s\"}"%name)
 
			if re.search(r'(?mis)10-K<\/td>',data):
				lists = re.findall(r'(?mis)10-K<\/td>[^>]*><a\shref\=\"([^\"]+)\"',data)
				for lis in lists:
					lis = re.sub(r'^','http://www.sec.gov',lis)
					lis = re.sub(r'amp\;',r'',lis)
					print (lis)


			

			
							
		print (data_store)
		writer.writerow( (data_store) )		


timy = time.strftime("%Y")
timm = time.strftime("%m")
timd = time.strftime("%d")
sleep = 2
output = Out()
output.links_extract("https://www.googleapis.com/youtube/v3/search?part=snippet&topicId=/m/016clz,/m/06by7,/m/031p9l,/m/0mz2,/m/01_bkd,/m/0gls8_3,/m/0ckz8q,/m/04sgwr,/m/02700bq,/m/017l9p,/m/012yc,/m/0gywn,/m/06mkbx,/m/0269_z,/m/02ltlq,/m/08jw93,/m/041738,/m/036dh5,/m/027mvm,/m/039mk,/m/02s5tv,/m/03qsdpk,/m/035m6,/m/025sf9q,/m/02w4v,/m/0584z,/m/01khrx,/m/07ssw,/m/0270gj,/m/0k5b5,/m/05229,/m/03lty,/m/0gg8l,/m/02wmv9,/m/0257h9,/m/0219x_,/m/0c41nfq,/m/04jly0w,/m/02vrljl,/m/06573d,/m/04g5k0,/m/06j6l,/m/06by7,/m/02yv6b,/m/04qf57,/m/06x6s,/m/02_8z3,/m/023fb,/m/01yhm,/m/03lcss,/m/036g9b,/m/0175zl,/m/04rlf,/m/016j4b,/m/095lwx,/m/064t9,/m/0d608,/m/01vvs2h,/m/05w3f,/m/01cvtf,/m/017541,/m/01750n,/m/025sc50,/m/05ztf3,/m/05h8jr,/m/016hv6,/m/0145rs,/m/02mscn,/m/0jlkq,/m/0qjh5,/m/01y0s9,/m/01m7k,/m/05r5c,/m/02rvwt,/m/04qf57,/m/01wtlq,/m/01gjqb,/m/01yrj,/m/02ntlj,/m/015vgc,/m/01tg5,/m/02l341,/m/02721m,/m/04h9h,/m/0349s,/m/0x2wv,/m/01_t8,/m/01fs_k,/m/03nmzqx,/m/01m7k,/m/05r5c,/m/02rvwt,/m/04qf57,/m/01wtlq,/m/01gjqb,/m/01yrj,/m/02ntlj,/m/015vgc,/m/01tg5,/m/02l341,/m/02721m,/m/04h9h,/m/0349s,/m/0x2wv,/m/01_t8,/m/01fs_k,/m/03nmzqx,/m/0ggx5q,/m/026bk,/m/08cyft,/m/064t9,/m/0c7fr,/m/035wcs,/m/02lnbg,/m/0kz10,/m/018rn4,/m/0335ws,/m/026pys,/m/041738,/m/04dn71w,/m/0bxdf,/m/06rrc,/m/03_3d,/m/01_zvr,/m/05c19l_,/m/03ppgp,/m/0gv832,/m/06mr2s,/m/02gbj,/m/0119_9kf,/m/0h1bpm6,/m/03j6x6,/m/033svp,/m/080twn,/m/05r336,/m/04jr23,/m/02r7xfs,/m/0hzmt37,/m/01xqnt,/m/02wxsk_,/m/0326g,/m/043dz8,/m/0ndhgst,/m/052bhm,/m/081js,/m/08vlns,/m/05k90v,/m/01j_ys,/m/02zs97,/m/01yzp0,/m/0127k62,/m/01f09r,/m/08ml73,/m/02fm82,/m/07s72n,/m/0dnr3sc,/m/0827v,/m/0g71l6z,/m/0135wsfx,/m/0g6gz1c,/m/010yb279,/m/0h1gyly,/m/0y4zc27,/m/0zpd8z_,/m/0qgx30n,/m/01335664,/m/0nmj1gp,/m/0qcjj3r,/m/013bg22h,/m/0dpwbxy,/m/0f2693x,/m/0rrhcck,/m/0_dv2x4,/m/0nh9mdv,/g/11b8tsz0_v,/m/012_lg5v,/m/0137_6sv,/m/0slfrkx,/m/0qhfjbl,/m/0nrjx11,/m/0gyr5f5,/m/0x63wr4,/m/0y4zcqt,/m/0nlx2d7,/m/0q6rc61,/m/0g6r67m,/m/0g2241m,/m/0x852qz,/m/0xcqx5c,/m/013by1nz,/m/0np3qmj,/m/0sj2cqq,/m/0nr3k3s,/m/011z9nq7,/m/0f0w8p_,/m/0nn7sx6,/m/0np5vdf,/m/0gbhrz_,/m/0ns4ztj,/m/0_k22ct,/m/0nhqtw3,/m/0nkl1b2,/m/0nsmbp0,/m/0_f04q5,/m/0f0w8lf,/m/011mz08t,/m/0x7rv39,/m/0qf_dr0,/m/0qbjgbf,/m/0mffy8k,/m/0fy3vy9,/m/0g7k3_s,/m/0qjw7lf,/m/0rthrfb,/m/0nt3z5s,/m/0d_vrxv,/m/0rsgcmk,/g/11bvt_rt08,/m/0nt36jb,/m/0111qzz8,/m/0q5w6_l,/m/0qhhz2k,/m/0fw_wf5,/m/011mwwyf,/m/0nnts_n,/m/0wm4qm3,/m/0rr4cgw,/m/0126xgtm,/m/0102263t,/m/0g22m4w,/m/0nlgbq2,/m/0q9534r,/m/011d0w9d,/m/01022l2d,/m/0_wttk2,/m/0rrjhj3,/m/0nklctm,/m/011mp4bn,/m/0_rxj1c,/m/0fgjc66,/m/018y50v,/m/0q6yqdw,/m/0xct7vy,/m/0nmqns1,/m/0qjrrxx,/m/0g7fczv,/m/0nkz9yg,/m/010dxdk_,/m/012kgshf,/g/11b824cq5h,/m/011fg1dt,/m/0nt0m72,/m/0nmx7_h,/m/0zr15l_,/m/0tqfgjh,/m/0zpf6qy,/m/0fvxl77,/m/010dxmfq,/m/0sjdgd9,/m/010tzsg0,/m/011272qw,/m/0nl9msr,/m/0gdtq6n,/m/0q8g4wh,/m/0np66x4,/m/0zvq8_f,/m/0np4bjc,/m/0zss0dg,/m/0_6f8sz,/m/01rg2bs,/m/0xbfn9x,/m/0ntbq9y,/g/11b82183mx,/g/11b821mj5w,/g/11b822kl2b,/g/11b822pgjs,/g/11b821ww47,/g/11b822mws7,/g/11b821tc35,/g/11b8226294,/g/11b822qb5l,/g/11b822jrzk,/g/11b822mwpk,/m/0qjq0zg,/m/0xqngmc,/m/0xdb9qm,/m/0xf9bqx,/m/0w04h9b,/m/013054xx,/m/0nnczn8,/m/0xhhqns,/m/034zxj5,/m/0fx5tk6,/m/0x7bfl4,/m/0qcllj0,/m/0g6r67g,/m/0qcllj0,/m/0g6r67g,/m/0q74z1s,/m/0ytddcm,/m/0dtcqdz,/m/0g0c0y9,/m/0q5vsjr,/m/0qg25v2,/m/0gdxn1z,/m/0fwpsmz,/g/12mkyf0gz,/m/0np42c9,/m/012887df,/m/0x6p8sb,/m/0tmpqbb,/m/0qbqh7y,/m/0132nqcj,/m/0x6byh3,/g/11b821mj7g,/g/11b822d_8t,/m/0slxvh7,/m/0yczs3q,/m/0fxvhr9,/m/0dyvdg_,/m/010dj5ps,/m/0q9g7zt,/m/0nlv37k,/m/0fydffc,/m/0zp64xq,/m/0qdkdyw,/m/0122hh87,/m/0slm3l2,/m/0nq0_lr,/m/0g7k3_z,/m/0135p25b,/m/0qdkp5k,/m/0nmb51w,/m/0g728sp,/m/0fzdcs4,/m/0qcjbby,/m/0nmp2rv,/m/0q6_5p6,/m/0zvr4l3,/m/0q75w3h,/m/01lyv,/m/016zgj,/m/0mhfr,/m/0c7fr,/m/04_mpy,/m/06mkj,/m/01crd5,/m/06npd,/m/03gyl,/m/03ryn,/m/0hzlz,/m/017510,/m/07f_yp,/m/04xn_,/m/017srm,/m/07ppd,/m/0y3_8,/m/0122042b,/m/03xnwz,/m/0336k21,/m/0glt670,/m/08q2hm,/m/031jp6n,/m/0zs8nm4,/m/04d3rwt,/m/04ff8tc,/m/0f4qp11,/m/0q7117z,/m/01gkk0q,/m/0fxqcr2,/m/04fg8s1,/m/0nyykh,/m/0y2tt7,/m/0ybbg41,/m/0fr3d6p,/m/023dwrn,/m/0p8jk0,/m/0zhlp9g,/m/01gj9z5,/m/032dk97,/m/0zslfk9,/m/0nt5cvb,/m/0x8_lql,/m/031z5wl,/m/02yh8l,/m/0rrrltd,/m/0374vxt,/m/0l4fnm1,/m/012pxxtk,/m/0f59d8y,/m/0fxqcpw,/m/0zpwxwp,/m/0ggx5q,/m/01gjdm2,/m/0ftj3pr,/m/02lnbg,/m/0x8rzgq,/m/01fn5x1,/m/019m82n,/g/11b7_lrxvh,/g/11b822l9pf,/g/11b822q9wy,/g/11b82184fx,/g/11b8216j0w,/g/11b8228rjv,/g/11b822kkrs,/g/11btzwxf1p,/m/0zq8xvm,/g/11btzx5dw1,/m/0g7htlw,/m/0g6wm_n,/m/012qcp17,/m/0f59dc7,/m/09sfzp1,/g/11bv0r9qmg,/g/11b815_54t,/g/11bytk1xf4,/m/0bjgzl4,/m/0p7c874,/m/040k8s,/m/0dm254r,/m/01qf_y6,/m/011q3_wk,/m/08cyft,/m/0l14qv,/m/01m3v,/m/01vdm0,/m/02qjv,/m/0m0jc,/m/0l14md,/m/03l65k,/m/01g1rg,/m/08mh3kd,/m/0122042b,/m/063syt,/m/026fx1,/m/04tbpp,/m/0y3_8,/m/02m96,/m/03ckfl9,/m/0163zw,/m/0ggx5q,/m/02nvq,/m/027fq_5,/m/020s1,/m/04_tb,/m/01jlc01,/m/01btfg,/m/0g6130,/m/08nq8w,/m/04b150,/m/02qml5k,/m/041738,/m/067_f8,/m/06by7,/m/09r48,/m/0gjkl,/m/02r3bh,/m/01_jx_,/m/03mg7c,/m/0jf72,/m/01n697,/m/0c2wf,/m/08xtsg,/m/04k6c,/m/0b__f0m,/m/029kh,/m/08dkdf,/m/08cyft,/m/0l14qv,/m/01m3v,/m/01vdm0,/m/02qjv,/m/0m0jc,/m/0l14md,/m/03l65k,/m/01g1rg,/m/08mh3kd,/m/0122042b,/m/063syt,/m/026fx1,/m/04tbpp,/m/0y3_8,/m/02m96,/m/03ckfl9,/m/0163zw,/m/0ggx5q,/m/02nvq,/m/027fq_5,/m/020s1,/m/04_tb,/m/01jlc01,/m/01btfg,/m/0g6130,/m/08nq8w,/m/04b150,/m/02qml5k,/m/041738,/m/067_f8,/m/06by7,/m/09r48,/m/0gjkl,/m/02r3bh,/m/01_jx_,/m/03mg7c,/m/0jf72,/m/01n697,/m/0c2wf,/m/08xtsg,/m/04k6c,/m/0b__f0m,/m/029kh,/m/08dkdf,/m/0glt670,/m/07t13s,/m/0q414c7,/m/021dsh,/m/0rr57k,/m/02y74y,/m/01flzq,/m/0zwjsjj,/m/05ydn_,/m/0jt63sg,/m/0xrc02,/m/01ndsk9,/m/0fvg_16,/m/0h132q_,/m/0l8qrvv,/m/0x1vtn,/m/017b11g,/m/0112fy0g,/m/0wq8dx9,/m/0zn36j,/m/027b1v7,/m/0skc46n,/m/0qdj0bx,/m/0_wtj_w,/m/0sh_wr3,/m/0nl4fn3,/m/01bws40,/m/0nlkkkj,/m/0p3mw1,/m/033159,/g/11bv1mbjt3,/m/011pj18z,/m/03gftq8,/m/0nmqxbf,/m/0132y2,/m/07mrpn,/m/0f6vwcf,/m/010slmfp,/m/0fsgtjt,/m/0fz7_sq,/m/01rm7r3,/m/0fxd98z,/m/010k7q4y,/m/0_6bc01,/m/037x3rf,/m/0xngnxj,/m/0_56ct,/m/015dnkx,/m/0skb4s7,/m/0x0lq95,/m/0120f92d,/m/0gb9_ry,/m/09tm98,/m/0wt716l,/m/013nbdl,/m/01gr15k,/g/11bv1lw32x,/m/014chlp,/m/0nlk6dx,/m/0frzn_n,/m/0457hmt,/m/0sh2fvl,/m/014sv81,/m/0c3fwk,/m/0f0jhyh,/m/010j1fr3,/m/0dyrgm3,/m/0t0nd8,/m/0f9cx91,/m/0_6421b,/m/0fqhwf5,/m/0gdzypl,/m/0qh2k3f,/m/03150c6,/m/0snxkf4,/m/02x19yl,/m/0dwrwc4,/m/03gf65y,/m/0bg539,/m/0wvhysq,/m/0tnnp17,/m/0g1vs39,/m/0103r6f,/m/0dp5w5r,/m/016994g,/m/0nnt2wb,/m/0193s3d,/m/010jg1ws,/m/0_65wb3,/m/01k8h_p,/m/0ylt6_,/m/0x6_nl_,/m/0nldt7z,/m/0188fzy,/m/0dtpvw7,/m/0fvj5jk,/m/0gb9_q_,/m/0nmdmpf,/m/0fkhx4w,/m/0dw_w2t,/m/01bwhv7,/m/010dl406,/m/0qdfp95,/m/0fscgz0,/m/0gdw322,/m/0gb9_rq,/m/0nm7b4y,/m/012_x9qd,/m/0242zrw,/m/0g5mlxd,/m/0dpsy4g,/m/0z0h7r,/m/0dtlpdk,/m/0yxf64x,/m/0fw_19h,/m/012xxb4k,/m/01k29xm,/m/03fpl_s,/m/0fxjjfs,/m/0tm32xb,/m/03frw0g,/m/011s2kbx,/m/0rrw7j6,/m/01rjbfp,/m/035ffgd,/m/0fty55z,/m/0nnw3r5,/m/013b72_,/m/0fty55z,/m/0nnw3r5,/m/013b72_,/m/01k4qjp,/m/0y91bmh&publishedAfter={0}-{1}-{2}T00%3A00%3A00Z&type=video&key=AIzaSyAnimLnprBHU5BVrd_61ynch4x5gPzrsPA".format(timy,timm,timd))
#output.dedup_one()
#output.data_extract()
#output.dedup_two()
#output.main_data_to_csv()


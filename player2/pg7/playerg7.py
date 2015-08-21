import threading
import urllib.request
import os
import re
import time
import json
import sys

class Facebook(object):

	while True:
		try:

			def wget(self,url):
				#self.url = url 
				self.data = os.popen('wget -qO- %s'% url).read()
				return self.data

			def wget_sepcial(self,url):
				self.data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
				return self.data

			def curl(self,url):

				self.url = url 
				self.data = os.popen('curl --silent --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" %s >/dev/null'% self.url).read()
				return self.data

				#print (self.data)

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


class Out(Facebook):

	def crawl_fb_artist_bio(self,sleep):
		#data = <h2 class="page_location_name">
		f2 = open('facebook_crawled_urls','a')
		f3 = open('crawled_email1','a')
		f4 = open('facebook_urls_crawl_report.json','a')
		a = 60000
		while True:
			a = a + 1
			aurls = "https://player.me/api/v1/games/%s" % a
			if re.search(r'^htt',aurls):
				lin = re.sub(r"\s*","",aurls)
				print (lin)
				sleep
				try:
					output.wget_sepcial(aurls)
					data = self.data 
					data = str(data)
				#print (data)
					length = len(data)
				#print (length)
				#print (data)
					#if a == 3800000:
					if a == 70000:
						#771735
						break
					#print ("hi")
					else:
						if re.search(r'(?ms)url\"\:\"\\([^\"]*)\"',data):
							link = re.findall(r'(?ms)url\"\:\"\\([^\"]*)\"',data)[0]
							link = re.sub(r'^','https://player.me',link)
							f4.write("{\""+lin+"\" => \""+link+"\"}"+"\n")
							print (link)
							output.web_extract(link)
						else: 
							f4.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")

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
						  

				except Exception: 
					pass  


	def web_extract(self,url):
		f1 = open('crawled_web_link','a')
		f2 = open('facebook-crawled_email_ids_report.json','a')
		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data)

				if re.search(r'(?mis)profile\-\-link\-facebook\"\shref\=\"([^\"]*)\"',data):
					link = re.findall(r'(?mis)profile\-\-link\-facebook\"\shref\=\"([^\"]*)\"',data)[0]
					print (link)
					f1.write(link+"\n")
					f2.write("{\""+lin+"\" => \""+link+"\"}"+"\n")
					output.crawl_fb_again_again(link)

				if re.search(r'(?mis)profile\-\-link\-web\"\shref\=\"([^\"]*)\"',data):
					link = re.findall(r'(?mis)profile\-\-link\-web\"\shref\=\"([^\"]*)\"',data)[0]
					print (link)
					f1.write(link+"\n")
					f2.write("{\""+lin+"\" => \""+link+"\"}"+"\n")
					output.crawl_fb_again(link)

			except Exception: 
					pass 

	def crawl_fb_again_again(self,url):
		#f1 = open('facebook_crawled_urls','r+')
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled1_email_ids_report.json','a')
		if re.search(r'^htt',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
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

				if re.search(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data):
					email = re.findall(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data)
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


				else: 
					print ("not found")
					f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
			except Exception: 
				pass

		if re.search(r'^htt',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				output.urllib(lin)
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
									output.urllib(url)
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

				if re.search(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data):
					email = re.findall(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data)
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
									output.urllib(url)
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


				else: 
					print ("not found")
					f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
			except Exception: 
				pass

	def crawl_fb_again(self,url,sleep):
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
				#print (url_lin)
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

	#def dedup_email(self):
	 #   with open('crawled_email1') as result:
	  #     uniqlines = set(result.readlines())
	   #     with open('crawled_email1', 'w') as rmdup:
		#        rmdup.writelines(set(uniqlines))

					  
		

sleep = 2
output = Out()

output.crawl_fb_artist_bio(sleep)
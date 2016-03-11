import xmlwitch 
import requests 
import xml.etree.ElementTree as ET 
 
 
explainUrl='https://sandbox02-eu.alma.exlibrisgroup.com/view/sru/47BIBSYS_UBO?version=1.2&operation=explain' 
response = requests.get(explainUrl) 

 
root = ET.fromstring(response.text) 

 
ns = {'e20' : 'http://explain.z3950.org/dtd/2.0/', 
      'e21' : 'http://explain.z3950.org/dtd/2.1/'} 

 
indexes = root.findall('.//{http://explain.z3950.org/dtd/2.0/}index') 
len(indexes) 

 
print '%40s %s' % ('NAME', 'DESCRIPTION') 
for index in indexes: 
    title = index.find('e21:title' , ns).text 
    name = index.find('.//e20:name' , ns).text 
    print ' %40s %s' % (name,title) 

# searchUrl='https://sandbox02-eu.alma.exlibrisgroup.com/view/sru/47BIBSYS_UBO' 
#  mineparametre={ 
#   'version': '1.2', 
#             'operation': 'searchRetrieve', 
#             'query': 'alma.subjects=Monstre', 
#             'maximumRecords': '20', 
#     } 


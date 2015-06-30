## trac gunicorn

~~~
# gunicorn -c path_to/guniconf.py guniconf:application                              
#                                                                                   
import os                                                                           
import sys                                                                          
                                                                                    
# Params                                                                            
BASE_DIR = os.path.join(                                                            
    os.path.dirname(os.path.abspath(__file__)))                                     
sys.stdout = sys.stderr                                                             
                                                                                    
# Gnicorn                                                                           
sys.path.append(BASE_DIR)                                                           
                                                                                    
# logs                                                                              
LOGS = os.path.join(BASE_DIR, 'log')                                                
if not os.path.isdir(LOGS):                                                         
        os.makedirs(LOGS)                                                           
                                                                                    
# Gunicorn Configuration                                                            
bind = os.environ.get('TRAC_BIND', "127.0.0.1:9000")                                
accesslog = os.path.join(LOGS, "gunicorn.access.log")                               
errorlog = os.path.join(LOGS, "gunicorn.error.log")                                 
proc_name = "trac.{0}".format(os.path.basename(BASE_DIR))                           
                                                                                    
                                                                                    
# TRAC                                                                              
                                                                                    
CACHE = os.path.join(BASE_DIR, '.eggs/')                                            
if not os.path.isdir(CACHE):                                                        
    os.mkdir(CACHE)                                                                 
                                                                                    
os.environ['TRAC_ENV'] = BASE_DIR                                                   
# os.environ['TRAC_ENV_PARENT_DIR'] = os.path.dirname(BASE_DIR) # Multi Projects 
os.environ['PYTHON_EGG_CACHE'] = CACHE                                              
                                                                                    
                                                                                    
def application(environ, start_response):                                           
    import trac.web.main                                                            
    environ['REMOTE_USER'] = environ.get('HTTP_REMOTE_USER')                        
    return trac.web.main.dispatch_request(environ, start_response)                  
~~~
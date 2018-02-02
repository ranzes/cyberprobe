
import socket
import json

class Client:

    def __init__(self, host, port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        self.sock = s

    def send(self, req):
        data = json.dumps(req) + "\n"
        self.sock.send(data)
        resp = self.sock.makefile().readline()
        resp = json.loads(resp)
        return resp

    def auth(self, user, p):
        req = {"command":"auth", "username":user, "password":p}
        resp = self.send(req)
        if resp["status"] == "200":
            return

        raise RuntimeError(resp["message"])

    def get_interfaces(self):
        req = {"command":"interfaces"}
        resp = self.send(req)
        if resp["status"] != "201":
            raise RuntimeError(resp["message"])

        l = []

        for v in resp["response"]:
            i = resp["response"][v]
            l.append(i)

        return l
    
    def get_endpoints(self):
        req = {"command":"endpoints"}
        resp = self.send(req)
        if resp["status"] != "201":
            raise RuntimeError(resp["message"])

        l = []

        for v in resp["response"]:
            i = resp["response"][v]
            l.append(i)

        return l
    
    def get_parameters(self):
        req = {"command":"parameters"}
        resp = self.send(req)
        if resp["status"] != "201":
            raise RuntimeError(resp["message"])

        l = []

        return resp["response"]

    def get_targets(self):
        req = {"command":"targets"}
        resp = self.send(req)
        if resp["status"] != "201":
            raise RuntimeError(resp["message"])

        l = []

        for v in resp["response"]:
            i = resp["response"][v]
            l.append(i)

        return l
        
    def add_interface(self, interf, delay=0.0, filter=None):

        req = {"command":"add-interface", "interface": interf}
        if delay > 0.0: req["delay"] = delay
        if filter: req["filter"] = filter
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])
        
    def remove_interface(self, interf, delay=0.0, filter=None):

        req = {"command":"remove-interface", "interface": interf}
        if delay > 0.0: req["delay"] = delay
        if filter: req["filter"] = filter
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])
        
    def add_target(self, liid, address, cls="ipv4", network=None):

        req = {"command":"add-target", "liid": liid, "address": address,
               "class": cls}
        if network: req["network"] = network
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])
        
    def remove_target(self, liid, address, cls="ipv4", network=None):

        req = {"command":"remove-target", "liid": liid, "address": address,
               "class": cls}
        if network: req["network"] = network
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])
        
    def add_endpoint(self, host, port, type, transport="tcp", key=None,
                     cert=None, chain=None):

        req = {"command":"add-endpoint", "host": host, "port": port,
               "type": type, "transport": transport}
        if key: req["key"] = key
        if cert: req["key"] = cert
        if chain: req["key"] = chain
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])

    def remove_endpoint(self, host, port, type, transport="tcp", key=None,
                     cert=None, chain=None):

        req = {"command":"remove-endpoint", "host": host, "port": port,
               "type": type, "transport": transport}
        if key: req["key"] = key
        if cert: req["key"] = cert
        if chain: req["key"] = chain
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])

    def add_parameter(self, key, value):

        req = {"command":"add-parameter", "key": key, "value": value}
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])

    def remove_parameter(self, key, value):

        req = {"command":"remove-parameter", "key": key, "value": value}
            
        resp = self.send(req)
        if resp["status"] != "200":
            raise RuntimeError(resp["message"])

    def close(self):
        resp = self.send({"command":"quit"})
        self.sock.close()
        self.sock = None

        
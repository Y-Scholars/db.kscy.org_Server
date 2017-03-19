# db.kscy.org_Server
Y Schola Web DB : Archive for KSCY researches

How to see apidoc
~~~
//install
npm install apidoc -g

//run
apidoc -i myapp/ -o apidoc/ -t mytemplate/
~~~

### Memo

- There are two ways for installing elasticsearch. 
 * With packages such as apt, yum
 
 * Manually download .deb and install it.
 
 In this ansible script, ansible installs elasticsearch with second way.
 
 The service for elasticsearch is in /etc/init.d
 
 

- Elasticsearch tries to allocate jvm heap 2gb basically.
To solve the issue of jvm memory allocations, go to /etc/elasticsearch/jvm.options and change -Xms, -Xmx
 * To see more information of elasticsearch's status, use 'sudo service elasticsearch status' command.

- The default directory for logstash is /usr/share/logstash/. Configuration files are in /etc/logstash directory
 

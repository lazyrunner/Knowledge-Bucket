# Website Hosting in Linux Machine

<b>Goal:</b> Start an apache server inside a remote linux machine and host a website and be able to access it from outside the network. This can also be visualised as <b>LAMP</b> architecture. But currently only L and A and P will be covered.

<b>Software Specification:</b> The linux machine is Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-118-generic x86_64)

## Apache Server 

<b>Goal: </b> Goal of this sub portion is to install the apache server (apache2 in ubuntu and debian) and testing if the installation is fine.

Install Apache2 server 

<pre><code>apt-get install apache2
</code></pre>

Once installation is done. To start , restart and stop 

<pre><code>/etc/init.d/apache2 start</code></pre>

<pre><code>/etc/init.d/apache2 restart</code></pre>

<pre><code>/etc/init.d/apache2 stop</code></pre>

To check status 

<pre><code>/etc/init.d/apache2 status</code></pre>

These commands can also be executed by <code>systemctl</code>.

<pre><code>systemctl [command] apache2</code></pre>

<b>Note:</b> To check if the apache server is running we need <code>curl http://your_server_ip</code> or <code>http://localhost</code>. To get the server ip, use <code>ifconfig</code> and get the ipv4 ip <code>inet</code> of the non lo adaptor.

Since our machine is remote machine, we had to do curl and not use the local browser as it is still not accessible outside the remote server network. However, if you are running it locally - you can do <code>http://your_server_ip</code>. This will be handled below by tunnel porting. 

## Hosting website 

<b>Goal:</b> This subsection will deal with hosting our own website in a custom domain server.Do note , we have not yet bought any server.

Till now the step we have accomplished is <code>curl http://your_server_ip</code> . What we should see here in our terminal/browser is a rendered html file containing details about the apache2 server. 

<b>Let us now try to understand how is that particular html file rendered. </b>

This particular html file is in <code>/var/www/html/</code>. All our websites should be inside the <code>/var/www/</code> folder. 

<b>Note:</b> If we want to change this html file. We have to rename the new html file index.html (atleast till now) and restart the server.

<b> Hosting our own domain and consequently own website </b>

We know that <code>http://localhost</code> gives us the index.html file inside the /var/www/html folder. However, this localhost is just a name given to the ip and needs to be mapped somewhere.
That somewhere is present in <code>/etc/hosts</code> file. 
Now we can add our own host as a new line or if the ip is already existing as another entry on that line.

<pre><code>
127.0.0.1 localhost [host_name]
</pre></code>

Now if we try <code>http://host_name</code>. It will render the index.html file inside /var/www/html folder. 

<b>The next step is to connect this to our website. </b>

For this let us first create a folder in /var/www/. Inside this folder , let us have any subfolder required or place our website file.

This folder/site now needs to be connected to the host. That is done in <code>/etc/apache2/sites-available</code>.Create a new file by copying <code>000-default.conf</code>. The name should be same as the host we want to create.
We are creating a virtual host . The sample (with comments can be found in virtualHost.conf)

Once this configuration file is created , we need to enable it. 

<code>a2ensite [configuration_file_name] </code>

What this does is create a symlink (file pointing to the conf file in sites-available) in <code>/etc/apache2/sites-enabled</code>. Then reload the apache2 server.

Post that <code>curl http://[host_name]</code> should give us the new website. 

## Port Tunneling

<b>Note:</b> This portion is very specific if you are not able to access the host or ip from outside the remote machine network/terminal

<b>Goal:</b> Tunnel the port (:80 in our case) so that we can access the website from outside the network 

<pre><code>ngrok http -host-header=rewrite [host_name]:[port]

Eg:
ngrok http -host-header=rewrite test.dev:80</code><pre>










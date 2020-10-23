# Commands used in windows 

####\#Author : Sudeshna Bora

### <a name="os_build">Get information about OS build</a>
<br>
<pre><code>
<b>Get-ComputerInfo | select WindowsProductName, WindowsVersion, OsHardwareAbstractionLayer</b>
<br>
<br>
WindowsProductName              WindowsVersion OsHardwareAbstractionLayer
------------------              -------------- --------------------------
Windows 10 Home Single Language 2004           10.0.20226.1000

</code></pre>

<b>cmdlet Documentation: </b> [Get-ComputerInfo Documentation](https://techcommunity.microsoft.com/t5/itops-talk-blog/powershell-basics-are-you-using-get-computerinfo/ba-p/482011)

### <a name="adaptor_status">Get Network Adaptor status</a>
<br>
<pre><code>
<b>Get-NetAdapter</b>
<br>
<br>
Name                      InterfaceDescription                    ifIndex Status       MacAddress             LinkSpeed
----                      --------------------                    ------- ------       ----------             ---------
Bluetooth Network Conn... Bluetooth Device (Personal Area Netw...      19 Disconnected B4-6B-FC-60-86-CC         3 Mbps
Wi-Fi                     Intel(R) Dual Band Wireless-AC 3165          18 Up           B4-6B-FC-60-86-C8     433.3 Mbps
vEthernet (WSL)           Hyper-V Virtual Ethernet Adapter             15 Disconnected 00-15-5D-46-41-42          0 bps
Ethernet                  Realtek PCIe GbE Family Controller           10 Disconnected 8C-16-45-4F-F5-B6          0 bps
Ethernet 2                Cisco AnyConnect Secure Mobility Cli...       7 Disabled     00-05-9A-3C-7A-00     431.1 Mbps
Ethernet 3                TAP-Windows Adapter V9                        3 Disconnected 00-FF-27-78-AC-CC       100 Mbps
</code></pre>

<b>What is a network adaptor: </b> hardware component(in motherboard chip) within a computer for interfacing or connecting with a network.

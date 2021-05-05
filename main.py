from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel 
# from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationItem
# from kivymd.uix.navigationdrawer import MDDesktopNavigationDrawer, MDNavigationLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivy.properties import ObjectProperty
import os
import webbrowser
import socket
# import ipaddress
# import netifaces
# import ipaddr
import struct
# from kivymd.uix.selection import MDCheckBox
import pyperclip
import wmi


class Share(BoxLayout):
    def copy(self, obj):
        pyperclip.copy('https://discord.gg/3EQRdmY')
        self.copy_layout.add_widget(MDLabel(text='Copied!',size_hint_x=.3))


class Pforward(BoxLayout):
    def get_ip(self):
        int_ip = socket.gethostbyname(socket.gethostname())
        self.ipitem.text = 'Your IP is: ' + str(int_ip)
        
    def launch_pf(self):
        webbrowser.open('https://portforward.com/router.htm')

class MacAddress(BoxLayout):
    def mac_ok_press(self, obj):
        mac1 = self.ids.malabel1.text
        mac2 = self.ids.malabel2.text
        mac3 = self.ids.malabel3.text
        mac4 = self.ids.malabel4.text
        macs = [mac1,mac2,mac3,mac4]

        macnums = []


        if (mac1 and mac2 and mac3 and mac4):
            count = 3
            for i in macs:
                if str(i).isalnum() and count%2 != 0:
                    if str(i) == 'a':
                        macnums.append(160)
                    elif str(i) == 'b':
                        macnums.append(176)
                    elif str(i) == 'c':
                        macnums.append(192)
                    elif str(i) == 'd':
                        macnums.append(208)
                    elif str(i) == 'e':
                        macnums.append(224)
                    elif str(i) == 'f':
                        macnums.append(240)
                    elif str(i) == '0':
                        macnums.append(0)
                    elif str(i) == '1':
                        macnums.append(16)
                    elif str(i) == '2':
                        macnums.append(32)
                    elif str(i) == '3':
                        macnums.append(48)
                    elif str(i) == '4':
                        macnums.append(64)
                    elif str(i) == '5':
                        macnums.append(80)
                    elif str(i) == '6':
                        macnums.append(96)
                    elif str(i) == '7':
                        macnums.append(112)
                    elif str(i) == '8':
                        macnums.append(128)
                    elif str(i) == '9':
                        macnums.append(144)

                elif str(i).isalnum() and count%2 == 0:
                    if str(i) == 'a':
                        macnums.append(10)
                    elif str(i) == 'b':
                        macnums.append(11)
                    elif str(i) == 'c':
                        macnums.append(12)
                    elif str(i) == 'd':
                        macnums.append(13)
                    elif str(i) == 'e':
                        macnums.append(14)
                    elif str(i) == 'f':
                        macnums.append(15)
                    elif str(i) == '0':
                        macnums.append(0)
                    elif str(i) == '1':
                        macnums.append(1)
                    elif str(i) == '2':
                        macnums.append(2)
                    elif str(i) == '3':
                        macnums.append(3)
                    elif str(i) == '4':
                        macnums.append(4)
                    elif str(i) == '5':
                        macnums.append(5)
                    elif str(i) == '6':
                        macnums.append(6)
                    elif str(i) == '7':
                        macnums.append(7)
                    elif str(i) == '8':
                        macnums.append(8)
                    elif str(i) == '9':
                        macnums.append(9)
                count += 1
            ip1 = macnums[0] + macnums[1]
            ip2 = macnums[2] + macnums[3]
            global ip
            ip = '10.253.' +str(ip1)+'.'+str(ip2)
            print(ip)
            MacAddressDialog.dismiss()
            Snackbar(text="MAC input successful!",snackbar_y='75dp').open()

class Main(MDApp):
    currentscreen = ObjectProperty()
    # global screen_manager
    # screen_manager = ScreenManager()
    def build(self):
        self.icon = 'discord-2.png'
        # Config.set('kivy', 'window_icon', 'discord-2.ico')
        self.title = 'Splinter Cell Online PS2 Setup Guide V3.0'
        global ip 
        ip = ' '
        global currentscreen
        currentscreen = self.root.ids.screen_manager.current
        self.theme_cls.primary_palette = 'Green'
        # print(self.screen_manager.screen_names)

    def back_button(self, screen):
        # self.root.ids.screen_manage.transition.direction = 'right'
        self.root.ids.screen_manager.current = screen

    def next_button(self, screen):
        # self.root.ids.screen_manage.transition.direction = 'left'
        self.root.ids.screen_manager.current = screen

    def ip_info(self, screen):
        # self.root.ids.screen_manage.transition.direction = 'left'
        # gws = netifaces.gateways()
        # gateway = gws['default'][netifaces.AF_INET][0]
        wmi_obj = wmi.WMI()
        wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
        wmi_out = wmi_obj.query( wmi_sql )
        for dev in wmi_out:
            gateway = dev.DefaultIPGateway[0]        # print(str(netifaces.gateways()))

        self.root.ids.ip_info.text = ip + '\n' + '255.255.0.0' + '\n' + str(gateway)
        self.root.ids.screen_manager.current = screen


    def mac_address_prompt(self):

        global MacAddressDialog

        if self.root.ids.screen_manager.current == 'console2':
            if ip != ' ':
                self.root.ids.screen_manager.current = 'console3'
            else:
                ma = MacAddress()
                self.dialog = MDDialog(
                    title="Select the last 4 digits of your MAC Address",
                    type="custom",
                    content_cls=ma,
                    buttons=[
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                        ),
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release = ma.mac_ok_press
                        ),
                    ],
                )
                MacAddressDialog = self.dialog
                self.dialog.open()
        else:
            if ip != ' ':
                self.root.ids.screen_manager.current = 'emulator7'
            else:
                ma = MacAddress()
                self.dialog = MDDialog(
                    title="Select the last 4 digits of your MAC Address",
                    type="custom",
                    content_cls=ma,
                    buttons=[
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                        ),
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color, on_release = ma.mac_ok_press
                        ),
                    ],
                )
                MacAddressDialog = self.dialog
                self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        
    def xlinkcheckpcsx2(self):
        if os.path.exists(os.path.expanduser('~') + '\\AppData\\Roaming\\XLink Kai\\'):
            self.root.ids.screen_manager.current = 'connection'
        else:
            webbrowser.open('https://www.teamxlink.co.uk/')
            self.root.ids.screen_manager.current = 'install-pcsx2'

    def xlinkinstallcheck(self):
        if os.path.exists(os.path.expanduser('~') + '\\AppData\\Roaming\\XLink Kai\\'):
            self.root.ids.screen_manager.current = 'register'
        else:
            webbrowser.open('https://www.teamxlink.co.uk/')
            self.root.ids.screen_manager.current = 'install'

    def xlinkregister(self):
        webbrowser.open('https://www.teamxlink.co.uk/u/register')
        self.root.ids.screen_manager.current = 'register1'
        
    def no_console(self):
        self.dialog = MDDialog(
            text="You will need to double-check your MAC Address and Console Settings",
            buttons=[
                MDFlatButton(
                    text="Close", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                ),
                MDFlatButton(
                    text="Go to Emulator", text_color=self.theme_cls.primary_color, on_release = self.gotoemulator
                ),
                MDFlatButton(
                    text="Go to Console", text_color=self.theme_cls.primary_color, on_release = self.gotoconsole
                ),
            ],
        )
        global ncDialog
        ncDialog = self.dialog
        self.dialog.open()

    def gotoconsole(self, obj):
        self.root.ids.screen_manager.current = 'console1'
        self.dialog.dismiss()
        # ncDialog.dismiss()

    def gotoemulator(self, obj):
        self.root.ids.screen_manager.current = 'emulator'
        self.dialog.dismiss()
        # ncDialog.dismiss()

    def staticipnumbers(self):
        int_ip = socket.gethostbyname(socket.gethostname())
        # ip_int = str(ipaddress.ip_interface(str(int_ip)))
        mask_length = 24
        mask = (1<<32) - (1<<32>>mask_length)   
        # print(str(socket.inet_ntoa(struct.pack(">L", mask))))
        #netmask = str(ipaddr.IPv4Network(ip_int))
        netmask = str(socket.inet_ntoa(struct.pack(">L", mask)))
        # gws = netifaces.gateways()
        # gateway = gws['default'][netifaces.AF_INET][0]
        wmi_obj = wmi.WMI()
        wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
        wmi_out = wmi_obj.query( wmi_sql )

        for dev in wmi_out:
            gateway = dev.DefaultIPGateway[0]        # print(str(netifaces.gateways()))
        # print(ip_int)
        # print(str(ipaddress.ip_interface(str(int_ip))))
        # print('2')
        # print(str(ipaddress.ip_network(str(int_ip))))
        # mask = ipaddr.IPv4Network(ip_int)
        # print(mask)
        # int_ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
        # netmask = netifaces.ifaddresses(ip_int)[netifaces.AF_INET][0]['netmask']
        # gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
        self.root.ids.staticiplabel.text = str(int_ip) + '\n' + str(netmask) + '\n' + str(gateway)
        self.root.ids.screen_manager.current = 'static4'

    def pforwardhelp(self):
            pf = Pforward()
            self.dialog = MDDialog(
                title="Port Forward Help",
                type="custom",
                content_cls=pf,
                buttons=[
                    MDFlatButton(
                        text="Close", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                    ),
                ],
            )
            self.dialog.open()

    def emuinstall(self):
        webbrowser.open('https://pcsx2.net/download/releases/windows.html')
        self.root.ids.screen_manager.current = 'emuinstall1'
    
    def scpsetup(self):
        webbrowser.open('https://scptoolkit.en.softonic.com/')
        self.root.ids.screen_manager.current = 'controller2'

    def webbrowser(self, url):
        webbrowser.open(url)

    def ip_info_pcsx2(self, screen):
        # self.root.ids.screen_manage.transition.direction = 'left'
        # gws = netifaces.gateways()
        # gateway = gws['default'][netifaces.AF_INET][0]
        wmi_obj = wmi.WMI()
        wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
        wmi_out = wmi_obj.query( wmi_sql )

        for dev in wmi_out:
            gateway = dev.DefaultIPGateway[0]        # print(str(netifaces.gateways()))

        self.root.ids.ip_info_pcsx2.text = ip + '\n' + '255.255.0.0' + '\n' + str(gateway)
        self.root.ids.ip_info_pcsx2_dev9.text = ip + '\n' + '255.255.0.0' + '\n' + str(gateway)
        self.root.ids.screen_manager.current = screen

    def webbrowser_emuparadise(self):
        webbrowser.open("https://www.emuparadise.me/Sony_Playstation_2_ISOs/Gran_Turismo_4_(USA)/150573")
        webbrowser.open("https://hackinformer.com/2018/08/21/workaround-to-download-roms-off-emuparadise-again/")

    def share(self):
        share = Share()
        self.dialog = MDDialog(
            title="Share this with friends!",
            type="custom",
            content_cls=share,
            buttons=[
                MDFlatButton(
                    text="CLOSE", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                ),
                MDFlatButton(
                    text="COPY LINK", text_color=self.theme_cls.primary_color, on_release = share.copy
                ),
            ],
        )
        self.dialog.open()

Main().run()
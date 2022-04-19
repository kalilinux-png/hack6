##import dbus
import notify2
##notify2.init('notification')
n = notify2.Notification(None)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10000)

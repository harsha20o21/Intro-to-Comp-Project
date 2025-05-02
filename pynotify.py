import pyinotify

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        print(f"File modified: {event.pathname}")

    def process_IN_CREATE(self, event):
        print(f"New file created: {event.pathname}")

    def process_IN_DELETE(self, event):
        print(f"File deleted: {event.pathname}")

wm = pyinotify.WatchManager()
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

watch_directory = '/home/seed/Desktop'
wm.add_watch(watch_directory, pyinotify.IN_MODIFY | pyinotify.IN_CREATE | pyinotify.IN_DELETE)

print(f"Monitoring changes in {watch_directory}...")
notifier.loop()

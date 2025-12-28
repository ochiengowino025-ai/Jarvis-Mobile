import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class JarvisRemoteLoader(App):
    def build(self):
        self.label = Label(
            text="[b]Jarvis OS: Cloud Link Initialized...[/b]", 
            markup=True,
            color=(0, 1, 0, 1) # Green Text
        )
        # Permanent Link to your Brain
        self.commander_url = "https://gist.githubusercontent.com/ochiengowino025-ai/acc4a87df11d9bdd7705660121d6d171/raw/jarvis_brain.py"
        
        Clock.schedule_once(self.sync_with_commander, 2)
        return self.label

    def sync_with_commander(self, dt):
        try:
            # SSL Verification Disabled (Fixes the crash)
            response = requests.get(self.commander_url, timeout=10, verify=False)
            
            if response.status_code == 200:
                self.label.text = "[b]✅ Online. Executing Soul Command...[/b]"
                exec(response.text, globals())
                from kivy.core.window import Window
                Window.clear()
                self.root = start_jarvis_os()
            else:
                self.label.text = f"[b]❌ Server Error: {response.status_code}[/b]"
        except Exception as e:
            self.label.text = f"[b]❌ Connection Failed: {str(e)}[/b]"

if __name__ == "__main__":
    JarvisRemoteLoader().run()
  

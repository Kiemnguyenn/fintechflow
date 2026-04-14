from src.utils import banner

class FintechFlowApplication:

    @staticmethod
    def run():
        banner.show_banner()
        print("[System] FintechFlow Data Platform is ready ...\n")

if __name__ == "__main__":
    FintechFlowApplication().run()
import json
import os

class TargetProductPipeline:
    def open_spider(self, spider):
        self.file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "json_files")
        os.makedirs(self.file_path, exist_ok=True)

    def process_item(self, item, spider):
        tcin = item.get("tcin")
        if tcin:
            file_name = f"{tcin}.json"
            file_path = os.path.join(self.file_path, file_name)
            with open(file_path, "w") as f:
                json.dump(dict(item), f, indent=4)
        return item

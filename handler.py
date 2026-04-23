from typing import List, Dict, Any

class Handler:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data

    def process(self) -> List[Dict[str, Any]]:
        return [self._process_item(item) for item in self.data]

    def _process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        item['processed'] = True
        return item

    def get_processed_data(self) -> List[Dict[str, Any]]:
        return [item for item in self.data if item.get('processed', False)]

    def reset_processing(self) -> None:
        for item in self.data:
            item['processed'] = False

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Item1'},
        {'id': 2, 'name': 'Item2'},
    ]
    handler = Handler(sample_data)
    processed = handler.process()
    processed_data = handler.get_processed_data()
    print(processed_data)
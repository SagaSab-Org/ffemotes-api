import os
import json

print('Validating data')

with open('data.json', 'r') as file:
    json_data = json.load(file)

data = json_data['data']


def main():
    for category, info in data.items():
        print(f'Validating {category}...')

        # Validate category icon exists
        icon_path = info['icon_path']
        if not os.path.exists(icon_path):
            raise Exception(f"Icon image file missing {icon_path}")

        # Validate images exists
        image_items = info['items']
        for image_item in image_items:
            image_path = image_item['path']

            if not os.path.exists(image_path):
                raise Exception(f"Image file missing {image_path}")


if __name__ == '__main__':
    main()

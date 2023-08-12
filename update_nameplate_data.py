import os
import json
from pylightxl import readxl

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

NAMEPLATE_IN_FILE = os.path.join(WORKING_DIR, 'NamePlateTransData.xlsx')
NAMEPLATE_FOLDER = os.path.join(WORKING_DIR, 'namePlate')
NAMEPLATE_OUT_FILE = os.path.join(WORKING_DIR, 'namePlate', 'namePlateTransData.json')
NAMEPLATE_DATA_FILE = os.path.join(WORKING_DIR, 'namePlate', 'namePlateData.json')

NAMEPLATE_LICENSE = 'LICENSE.md'
NAMEPLATE_DATA_DATA_KEY = 'data'
NAMEPLATE_DATA_UPDATE_COMIT_KEY = 'updateComitHash'

def stringToJson(filename : str, outputFile : str) -> None:

  wb = readxl(filename)

  xlsx_data = {}

  for name in wb.ws_names:

    sheat = wb.ws(name)

    row, col = sheat.size

    # 行を回す
    for i in range(2, row + 1):

      data = {}

      # i行目の1列目はキー
      key = sheat.index(i, 1)
      if key == "":
        continue

      # i行目j列がデータ、jは2以上であり2が0(英語)である
      for j in range(2, col + 1):
          cell_data = sheat.index(i, j)

          if type(cell_data) != str or cell_data == "":
            continue

          # I hate excel why did I do this to myself
          data[str(j - 2)] = cell_data.replace("\r", "").replace("_x000D_", "").replace("\\n", "\n")

      if data != {}:
        xlsx_data[key] = data

  with open(outputFile, "w") as f:
    json.dump(xlsx_data, f, indent=4)

def update_visor_data()-> None:

  visor_dir = os.listdir(NAMEPLATE_FOLDER)

  new_visor = {}
  new_visor[NAMEPLATE_DATA_UPDATE_COMIT_KEY] = ""

  for visor in visor_dir:

    if os.path.isdir(os.path.join(NAMEPLATE_FOLDER, visor)):

      visors = os.listdir(os.path.join(NAMEPLATE_FOLDER, visor))
      cleaned_visor = [add_visor.replace('.png', '') for add_visor in visors if add_visor != NAMEPLATE_LICENSE]
      new_visor[visor] = cleaned_visor


  with open(os.path.join(NAMEPLATE_DATA_FILE), mode='w') as visor_json:
    json.dump(
      new_visor,
      visor_json, indent=2, ensure_ascii=False)

def main()-> None:
  update_visor_data()
  stringToJson(NAMEPLATE_IN_FILE, NAMEPLATE_OUT_FILE)

if __name__ == "__main__":
  main()
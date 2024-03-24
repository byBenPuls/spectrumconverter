import xml.etree.ElementTree as ET
import sys, os, csv
from datetime import datetime


def XMLtoTXT(filename):
    try:
        print("Конвертирование начато...")
        print(filename)
        tree = ET.parse(filename)
        # import data from xml
        DT = tree.find('ResultDataList/ResultData/SampleInfo/Time').text
        VPC = tree.find('ResultDataList/ResultData/EnergySpectrum/ValidPulseCount').text
        TPC = tree.find('ResultDataList/ResultData/EnergySpectrum/TotalPulseCount').text
        MT = tree.find('ResultDataList/ResultData/EnergySpectrum/MeasurementTime').text

        N = 0

        # get datapoints from xml

        DP = list('')
        for elem in tree.iterfind('ResultDataList/ResultData/EnergySpectrum/Spectrum/DataPoint'):
            N += 1
        DP.append(elem.text)

        # manage Date, 0 - year, 1 - month, 2 - day
        DateList = DT.split('-')
        TimeList = DateList[2].split('T')
        DateList[2] = TimeList[0]

        # manage Time
        del TimeList[0]
        TimeList = TimeList[0].split('.')
        del TimeList[1]

        # Compute LiveTime
        LT = float(VPC) / float(TPC) * float(MT)

        # manage out file
        NewFileName = os.path.splitext(filename)
        NewFileName = NewFileName[0] + ".txt"

        f = open(NewFileName, "w+")
        f.write("DATE={}-{}-{}\n".format(DateList[2], DateList[1], DateList[0]))
        f.write("TIME={}\n".format(TimeList[0]))
        f.write("TLIVE={:.2f}\n".format(LT))
        f.write("TREAL={:.2f}\n".format(float(MT)))
        f.write("SPECTRTXT={}\n".format(N))

        for i in range(N):
            f.write(str(i + 1) + '\t' + str(DP[i]) + '\n')
            f.close()
            print("Конвертирование завершено!")
            input('Нажмите на любую клавишу для продолжения..')

    except Exception as e:
        print("Произошла ошибка при конвертировании XML спектра: ", e)
        error_code = input("Для продолжения нажмите клавишу Enter.. ")


def CSVtoTXT(filename, LT):
    try:
        print("Начато конвертирование...")
        # open and read csv
        csvfile = open(filename, 'r')
        csvdata = csv.reader(csvfile, delimiter=',')

        # get spectra data
        CHN = list()
        IMP = list()

        for row in csvdata:
            CHN.append(row[0])
            IMP.append(row[1])

        N = len(CHN)

        # get time and date
        created = os.stat(filename).st_ctime
        DT = str(datetime.fromtimestamp(created))

        # manage Date, 0 - year, 1 - month, 2 - day
        DateList = DT.split('-')
        TimeList = DateList[2].split(' ')
        DateList[2] = TimeList[0]

        # manage Time
        del TimeList[0]
        TimeList = TimeList[0].split('.')
        del TimeList[1]

        # manage out file
        NewFileName = os.path.splitext(filename)
        NewFileName = NewFileName[0] + ".txt"
        f = open(NewFileName, "w+")

        f.write("DATE={}-{}-{}\n".format(DateList[2], DateList[1], DateList[0]))
        f.write("TIME={}\n".format(TimeList[0]))
        f.write("TLIVE={:}\n".format(str(LT)))
        f.write("TREAL={:}\n".format(str(LT)))
        f.write("SPECTRTXT={}\n".format(N))

        for i in range(N):
            f.write(str(i + 1) + '\t' + str(int(IMP[i])) + '\n')

        f.close()

        print("Конвертирование завершено!")
        input('Нажмите на любую клавишу для продолжения..')
    except Exception as e:
        print("Произошла ошибка при конвертировании CSV спектра: ", e)
        error_code = input("Для продолжения нажмите клавишу Enter.. ")


# main
print("Spectrum Converter by Ben Puls [v1.00]")

if len(sys.argv) == 1:
    path = os.getcwd()
else:
    path = sys.argv[1]

for file in os.listdir(path):
    if file.endswith(".xml"):
        XMLtoTXT(os.path.join(path, file))
    if file.endswith(".csv"):
        LiveTime = input("Укажите время в секундах набора спектра: ".format(file))
        CSVtoTXT(os.path.join(path, file), LiveTime)


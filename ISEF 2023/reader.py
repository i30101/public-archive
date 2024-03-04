import csv

class Reader:
    # finds index of single header, returns index
    def findIndex(filepath, h):
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            if h in headers:
                return headers.index(h)


    # finds indeces of multiple headers, returns dictionary
    @staticmethod
    def findIndeces(filepath, h):
        indeces = {}
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            for header in h:
                if header in headers:
                    indeces[header] = headers.index(header)
        return indeces

    
    # finds indeces of headers given header, returns dictionary
    @staticmethod
    def processIndeces(l, h):
        indeces = {}
        for header in h:
            if header in l:
                indeces[header] = l.index(header)
        return indeces

    
    # extracts all data by row, returns 2D list
    @staticmethod
    def extractRows(filepath):
        rows = []
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        return rows

    
    # extracts all data by column, returns dictionary
    @staticmethod
    def extractColumns(cls, filepath):
        indeces = {}
        columnData = {}
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            indeces = cls.processIndeces(headers, headers)
            for header in headers:
                columnData[header] = []
            for row in reader:
                for header in indeces:
                    columnData[header].append(row[indeces[header]])
        return columnData


    # gets all data in column
    @classmethod
    def getColumn(cls, filepath, h):
        data = []
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            index = next(reader).index(h)
            for row in reader:
                data.append(row[index])
        return data



    # extracts data of given headers for every row, returns 2D list
    @classmethod
    def filterRows(cls, filepath, h):
        indeces = {}
        rowData = []
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            indeces = cls.processIndeces(headers, h)
            for row in reader:
                rowData.append([row[indeces[header]] for header in indeces])
        return rowData


    # extracts data in every column of given headers, returns dictionary
    @classmethod
    def filterColumns(cls, filepath, h):
        indeces = {}
        columnData = {}
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            indeces = cls.processIndeces(headers, h)
            for header in indeces:
                columnData[header] = []
            for row in reader:
                for header in indeces:
                    columnData[header].append(row[indeces[header]])
        return columnData


    # truncates file
    @staticmethod
    def truncate(filepath):
        f = open(filepath, "w", newline = "")
        f.truncate()


    # writes values in iterable into csv file
    # t: whether file is truncated or not (bool)
    # s: whether newline is added at end
    @staticmethod
    def write(filepath, d, t = True, s = False):
        f = open(filepath, "a", newline = "")
        if t:
            f = open(filepath, "w", newline = "")
            f.truncate()
        writer = csv.writer(f)
        writer.writerows(d)
        if s:
            writer.writerow([])
        f.close()

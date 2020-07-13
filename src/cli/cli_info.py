from terminaltables import AsciiTable

if __name__ == '__main__':

    title = 'Command Line Interface'
    TABLE_DATA = (
    ('Command', 'Discription'),
    ('facerec new', 'Add a new root face.'),
    ('facerec enable', 'Enable facerec back.'),
    ('facerec disable', 'Temporarily disable facerec, preserving the setup.'),
    ('facerec remove', 'Completely remove the facerec and the root faces.'),
    ('facerec --help', 'Get info of the CLI'),
    )

    table_instance = AsciiTable(TABLE_DATA, title)
    print(table_instance.table)


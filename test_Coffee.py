import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, Text, StringVar, IntVar
import Coffee

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.root.withdraw()
        Coffee.receiptText = Text(self.root)
        Coffee.txtYuzu = StringVar(value="0")
        Coffee.txtHintGinger = StringVar(value="0")
        Coffee.txtEspresso = StringVar(value="0")

        Coffee.var1 = IntVar(value=0)
        Coffee.var2 = IntVar(value=0)

        Coffee.checkboxTeaCost = MagicMock()
        Coffee.checkboxNoncoffeeCost = MagicMock()
        Coffee.checkboxCoffeeCost = MagicMock()
        Coffee.checkboxSubtotal = MagicMock()
        Coffee.checkboxIVA = MagicMock()
        Coffee.checkboxTotal = MagicMock()

    def tearDown(self):
        self.root.destroy()

    @patch('Coffee.filedialog.asksaveasfile')
    @patch('Coffee.messagebox.showinfo')
    def test_save(self, mock_showinfo, mock_asksaveasfile):
        mock_file = MagicMock()
        mock_asksaveasfile.return_value = mock_file
        Coffee.receiptText.insert('1.0', 'Test receipt content')
        Coffee.save()
        mock_file.write.assert_called_once_with('Test receipt content\n')
        mock_file.close.assert_called_once()
        mock_showinfo.assert_called_once_with('Information:', message='Receipt stored successfully')

    def test_receipt(self):
        Coffee.varTeaCost = 10
        Coffee.varNoncoffeCost = 20
        Coffee.varCoffeeCost = 30
        Coffee.subtotal = 60
        Coffee.iva = 7.2
        Coffee.total = 67.2
        Coffee.receipt()
        receipt_content = Coffee.receiptText.get('1.0', 'end-1c')
        self.assertIn('Total in Tea ---------------------------------------------------> €10', receipt_content)
        self.assertIn('Total in Non-Coffee ----------------------------------------> €20', receipt_content)
        self.assertIn('Total in Coffee -----------------------------------------------> €30', receipt_content)
        self.assertIn('Subtotal --------------------------------------------------------> €60', receipt_content)
        self.assertIn('IVA ---------------------------------------------------------------> €7.2', receipt_content)
        self.assertIn('FINAL TOTAL ------------------------------------------------> €67.2', receipt_content)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, Text, StringVar, IntVar
import Coffee

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.root= Tk()
        self.root.withdraw()
        Coffee.receiptText= Text(self.root)
        #tea
        Coffee.txtYuzu= StringVar(value="0")
        Coffee.txtHintGinger= StringVar(value="0")
        Coffee.txtJujubeGoji= StringVar(value="0")
        Coffee.txtLycheeOolong= StringVar(value="0")
        Coffee.txtGuavaJasmin= StringVar(value="0")
        Coffee.txtBlackLemon= StringVar(value="0")
        Coffee.txtMatchaLemon= StringVar(value="0")
        #non-coffe
        Coffee.txtChocolate= StringVar(value="0")
        Coffee.txtMatchaLatte= StringVar(value="0")
        Coffee.txtUbeOatLatte= StringVar(value="0")
        #coffee
        Coffee.txtEspresso= StringVar(value="0")
        Coffee.txtDoubleEspresso= StringVar(value="0")
        Coffee.txtAmericano= StringVar(value="0")
        Coffee.txtCapuccino= StringVar(value="0")
        Coffee.txtFlatWhite= StringVar(value="0")
        Coffee.txtLatte= StringVar(value="0")
        Coffee.txtMocha= StringVar(value="0")
        Coffee.txtBiscoffLatte= StringVar(value="0")
        Coffee.txtDalgonaLatte= StringVar(value="0")
        Coffee.txtBlackSesamLatte= StringVar(value="0")
        Coffee.txtInjeolmiOatLatte= StringVar(value="0")
        Coffee.txtPistacchioOatLatte= StringVar(value="0")

        Coffee.var1= IntVar(value=0)
        Coffee.var2= IntVar(value=0)
        Coffee.var3= IntVar(value=0)
        Coffee.var4= IntVar(value=0)
        Coffee.var5= IntVar(value=0)
        Coffee.var6= IntVar(value=0)
        Coffee.var7= IntVar(value=0)
        Coffee.var8= IntVar(value=0)
        Coffee.var9= IntVar(value=0)
        Coffee.var10= IntVar(value=0)
        Coffee.var11= IntVar(value=0)
        Coffee.var12= IntVar(value=0)
        Coffee.var13= IntVar(value=0)
        Coffee.var14= IntVar(value=0)
        Coffee.var15= IntVar(value=0)
        Coffee.var16= IntVar(value=0)
        Coffee.var17= IntVar(value=0)
        Coffee.var18= IntVar(value=0)
        Coffee.var19= IntVar(value=0)
        Coffee.var20= IntVar(value=0)
        Coffee.var21= IntVar(value=0)
        Coffee.var22= IntVar(value=0)

        Coffee.checkboxTeaCost= MagicMock()
        Coffee.checkboxNoncoffeeCost= MagicMock()
        Coffee.checkboxCoffeeCost= MagicMock()
        Coffee.checkboxSubtotal= MagicMock()
        Coffee.checkboxIVA= MagicMock()
        Coffee.checkboxTotal= MagicMock()

    def tearDown(self):
        self.root.destroy()

    @patch('Coffee.filedialog.asksaveasfile')
    @patch('Coffee.messagebox.showinfo')

    def test_save(self, mock_showinfo, mock_asksaveasfile):
        mock_file= MagicMock()
        mock_asksaveasfile.return_value= mock_file
        Coffee.receiptText.insert('1.0', 'Test receipt content')
        Coffee.save()
        mock_file.write.assert_called_once_with('Test receipt content\n')
        mock_file.close.assert_called_once()
        mock_showinfo.assert_called_once_with('Information:', message= 'Receipt stored successfully')

    def test_receipt(self):
        Coffee.varTeaCost= 10
        Coffee.varNoncoffeCost= 20
        Coffee.varCoffeeCost= 30
        Coffee.subtotal= 60
        Coffee.iva= 7.2
        Coffee.total= 67.2
        Coffee.receipt()
        receipt_content = Coffee.receiptText.get('1.0', 'end-1c')
        self.assertIn('Total in Tea ---------------------------------------------------> €10', receipt_content)
        self.assertIn('Total in Non-Coffee ----------------------------------------> €20', receipt_content)
        self.assertIn('Total in Coffee -----------------------------------------------> €30', receipt_content)
        self.assertIn('Subtotal --------------------------------------------------------> €60', receipt_content)
        self.assertIn('IVA ---------------------------------------------------------------> €7.2', receipt_content)
        self.assertIn('FINAL TOTAL ------------------------------------------------> €67.2', receipt_content)


    def test_grantotal(self):
        Coffee.textYuzu= MagicMock()
        Coffee.textYuzu.get.return_value= '2'
        Coffee.textHintGinger= MagicMock()
        Coffee.textHintGinger.get.return_value= '3'
        Coffee.textJujubeGoji= MagicMock()
        Coffee.textJujubeGoji.get.return_value= '4'
        Coffee.textLycheeOolong= MagicMock()
        Coffee.textLycheeOolong.get.return_value= '2'
        Coffee.textGuavaJasmin= MagicMock()
        Coffee.textGuavaJasmin.get.return_value= '2'
        Coffee.textBlackLemon= MagicMock()
        Coffee.textBlackLemon.get.return_value= '6'
        Coffee.textMatchaLemon= MagicMock()
        Coffee.textMatchaLemon.get.return_value= '1'
        Coffee.textChocolate= MagicMock()
        Coffee.textChocolate.get.return_value= '7'
        Coffee.textMatchaLatte= MagicMock()
        Coffee.textMatchaLatte.get.return_value= '3'
        Coffee.textUbeOatLatte= MagicMock()
        Coffee.textUbeOatLatte.get.return_value= '8'
        Coffee.textEspresso= MagicMock()
        Coffee.textEspresso.get.return_value= '9'
        Coffee.textDoubleEspresso= MagicMock()
        Coffee.textDoubleEspresso.get.return_value= '3'
        Coffee.textAmericano= MagicMock()
        Coffee.textAmericano.get.return_value= '1'
        Coffee.textCapuccino= MagicMock()
        Coffee.textCapuccino.get.return_value= '1'
        Coffee.textFlatWhite= MagicMock()
        Coffee.textFlatWhite.get.return_value = '2'
        Coffee.textLatte= MagicMock()
        Coffee.textLatte.get.return_value= '2'
        Coffee.textMocha= MagicMock()
        Coffee.textMocha.get.return_value= '2'
        Coffee.textBiscoffLatte= MagicMock()
        Coffee.textBiscoffLatte.get.return_value= '3'
        Coffee.textDalgonaLatte= MagicMock()
        Coffee.textDalgonaLatte.get.return_value= '6'
        Coffee.textBlackSesamLatte= MagicMock()
        Coffee.textBlackSesamLatte.get.return_value= '8'
        Coffee.textInjeolmiOatLatte= MagicMock()
        Coffee.textInjeolmiOatLatte.get.return_value= '4'
        Coffee.textPistacchioOatLatte= MagicMock()
        Coffee.textPistacchioOatLatte.get.return_value= '2'
        Coffee.grantotal()
        self.assertEqual(Coffee.varTeaCost, round(2*3.5 + 3*3.5 + 4*3.8 + 2*4.5 + 2*4.5 + 6*4.5 + 1*4.5, 2))
        self.assertEqual(Coffee.varNoncoffeCost, round(7*4 + 3*4.5 + 8*4.8, 2))
        self.assertEqual(Coffee.varCoffeeCost, round(9*2 + 3*3 + 1*2.5 + 1*3.5 + 2*4 + 2*3.8 + 2*4.5 + 3*4.5 + 6*4.9 + 8*4.8 + 4*5.2 + 2*5.4, 2))
        self.assertEqual(Coffee.subtotal, round(2*3.5 + 3*3.5 + 4*3.8 + 2*4.5 + 2*4.5 + 6*4.5 + 1*4.5 + 7*4 + 3*4.5 + 8*4.8 + 
                                                9*2 + 3*3 + 1*2.5 + 1*3.5 + 2*4 + 2*3.8 + 2*4.5 + 3*4.5 + 6*4.9 + 8*4.8 + 4*5.2 + 2*5.4, 2))
        self.assertEqual(Coffee.iva, round((2*3.5 + 3*3.5 + 4*3.8 + 2*4.5 + 2*4.5 + 6*4.5 + 1*4.5 + 7*4 + 3*4.5 + 8*4.8 + 
                                                9*2 + 3*3 + 1*2.5 + 1*3.5 + 2*4 + 2*3.8 + 2*4.5 + 3*4.5 + 6*4.9 + 8*4.8 + 4*5.2 + 2*5.4)*0.16, 2))
        self.assertEqual(Coffee.total, round((2*3.5 + 3*3.5 + 4*3.8 + 2*4.5 + 2*4.5 + 6*4.5 + 1*4.5 + 7*4 + 3*4.5 + 8*4.8 + 
                         9*2 + 3*3 + 1*2.5 + 1*3.5 + 2*4 + 2*3.8 + 2*4.5 + 3*4.5 + 6*4.9 + 8*4.8 + 4*5.2 + 2*5.4) * 1.16, 2))

if __name__ == '__main__':
    unittest.main()

from Bio.PDB import PDBParser, PDBIO, Select, Dice
import io

parser = PDBParser()
pdbio = PDBIO()

one_conf = io.StringIO()

# Bio.PDB.Structure object
structure = parser.get_structure("X", "6wzu.pdb")

class KeepOneConfOnly(Select): # Bio.PDB.PDBIO.Select
    def __init__(self, keepAltID):
        super().__init__()
        self.keepAltID = keepAltID

    def accept_atom(self, atom):
        if (not atom.is_disordered()) or atom.get_altloc() == self.keepAltID:
            atom.set_altloc(" ") # eliminate alt location ID before output
            return True
        return False

pdbio.set_structure(structure)
pdbio.save(one_conf, select=KeepOneConfOnly("A"))

# reset file pointer
one_conf.seek(0)
structure = parser.get_structure("X", one_conf)
pdbio.set_structure(structure)
sel = Dice.ChainSelector("A", 1, 5000)
pdbio.save("6wzu_chA_only.pdb", sel)

print("""
[i] PDB processed.
  (1) Alternative side chain conformations removed.
  (2) Only the protein heavy atoms have been kept.
""")

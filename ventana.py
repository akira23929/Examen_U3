#codigo 3 este es el lo que lleva el boton registro
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from ventana import *
def main():
    root = Tk()
    root.wm_title("mostrar lista")

    app = ventana(root)
    app.mainloop()

if __name__ == "__main__":
    main()

  # Herencia es mi Frame 
class Ventana(Frame):
   
       # Contructor 
    def __init__(self, master=None):
        super().__init__(master,width=600, height=259)
        self.master = master
        self.pack()
        self.create_widgets()
        #Crud 
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("normal")  
        self.id=-1
        
    def habilitarCajas(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtApellido.configure(state=estado)
        self.txtEdad.configure(state=estado)
        self.txtMascota.configure(state=estado)
        
    def habilitarBtnOper(self,estado):
        self.btnAgregar.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):             
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtEdad.delete(0,END)
        self.txtMascota.delete(0,END)
        self.txtNombre.delete(0,END)
        self.txtApellido.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)      

    def fAgregar(self):         
        # base de datos 
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        edad = self.txtEdad.get()
        mascota= self.txtMascota.get()
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="registrosbd")
        cursor = conexion.cursor()
        consulta = "INSERT INTO `registro`(`Nombre`, `Apellidos`, `Edad`, `Mascota`) VALUES (%s, %s, %s, %s)"
        valores = (nombre,apellido,edad,mascota)
        cursor.execute(consulta,valores)
        conexion.commit()
        cursor.close()
        self.insert_data()
        self.limpiarCajas()        
        self.txtNombre.focus()



    def fModificar(self):
        # Obtener los identificadores de las filas seleccionadas
        seleccion = self.tree.selection()
        # Obtener el primer identificador de la selección (si hay uno)
        if len(seleccion) > 0:
            item = seleccion[0]
            # Objetos
            nombre = self.txtNombre.get()
            apellido = self.txtApellido.get()
            edad = self.txtEdad.get()
            mascota= self.txtMascota.get()
            conexion = mysql.connector.connect(
            host= "localhost",
            user = "root",
            password = "",
            database = "registrosbd")
            cursor = conexion.cursor()
            sql = "UPDATE `registro` SET `Apellidos` = %s, `Edad` = %s, `Mascota` = %s WHERE `Nombre` = %s"
            valores = (apellido, edad, mascota, nombre)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()    
            self.txtNombre.focus()
            
            # Eliminar la fila correspondiente
            self.tree.delete(item)
            self.insert_data()
    
    def fEliminar(self):
        # Obtener los identificadores de las filas seleccionadas
        seleccion = self.tree.selection()
        # Obtener el primer identificador de la selección (si hay uno)
        if len(seleccion) > 0:
            # Variables 
            item = seleccion[0]
            datos = self.tree.item(seleccion[0])  # obtener los datos de la fila seleccionada
            nombre = datos['values'][0]  # obtener el valor de la columna 'Nombre'

            #Borrar datos de la BD
            conexion = mysql.connector.connect(
            host= "localhost",
            user = "root",
            password = "",
            database = "registrosbd")
            cursor = conexion.cursor()
            sql = "DELETE FROM `registro` WHERE `Nombre` = %s"
            valores = [nombre]
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()      
            self.txtNombre.focus()
            
            # Eliminar la fila correspondiente
            self.tree.delete(item)
            
        else:
            # Si no hay ninguna fila seleccionada, mostrar un mensaje de error
            messagebox.showerror("Error", "Debe seleccionar una fila para eliminar.")            

    def fCancelar(self):
        
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=259)        
        self.btnAgregar=Button(frame1,text="Agregar", command=self.fAgregar, bg="purple", fg="white")
        self.btnAgregar.place(x=5,y=50,width=80, height=30 )   

        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="purple", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)  

        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="purple", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=259)    

        lbl1 = Label(frame2,text="Nombre : ")
        lbl1.place(x=3,y=5)        
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=25,width=50, height=20)    

        lbl2 = Label(frame2,text="Apellido : ")
        lbl2.place(x=3,y=55)        
        self.txtApellido=Entry(frame2)
        self.txtApellido.place(x=3,y=75,width=100, height=20)   

        lbl3 = Label(frame2,text="Edad : ")
        lbl3.place(x=3,y=105)        
        self.txtEdad=Entry(frame2)
        self.txtEdad.place(x=3,y=125,width=100, height=20)    

        lbl4 = Label(frame2,text="Mascota : ")
        lbl4.place(x=3,y=155)        
        self.txtMascota=Entry(frame2)
        self.txtMascota.place(x=3,y=175,width=50, height=20)   

        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="orange", fg="white")
        self.btnCancelar.place(x=10,y=210,width=60, height=30)   

        frame3 = Frame(self,bg="white" )
        frame3.place(x=247,y=0,width=520, height=500)     
         # mostrar tabla    
        self.tree = ttk.Treeview(frame3, columns=("nombre", "apellido", "edad", "mascota"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("apellido", text="Apellido")
        self.tree.heading("edad", text="Edad")
        self.tree.heading("mascota", text="Mascota")
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("#1", width=60, minwidth=60, anchor=CENTER)
        self.tree.column("#2", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#3", width=90, minwidth=90, anchor=CENTER)
        self.tree.column("#4", width=90, minwidth=90, anchor=CENTER)

        self.tree.grid(row=0, column=0, sticky="nsew")

    def insert_data(self):
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        edad = self.txtEdad.get()
        mascota = self.txtMascota.get()
        if nombre and apellido and edad and mascota:
            # Insertar los datos en la base de datos o en una lista
            # ...
            
            # Agregar los datos a la tabla
            self.tree.insert("", "end", text="1", values=(nombre, apellido, edad, mascota))
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos")
            
ventana = Tk()
app = Ventana(master=ventana)
app.mainloop()
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

def main():
    programacion = ["Software tradicional", "Machine Learning", "Computer Science"]
    estadistica = ["Estadística", "Machine Learning", "Investigación tradicional"]
    dominio_negocio = ["Conocimiento del negocio", "Investigación tradicional", "Software tradicional"]
    venn = venn3([set(programacion), set(estadistica), set(dominio_negocio)],
                 ("Programación", "Estadística", "Dominio negocio"))


    st.title("Diagrama de Venn")
    fig, ax = plt.subplots()
    venn = venn3([set(programacion), set(estadistica), set(dominio_negocio)],
                 ("Programación", "Estadística", "Dominio negocio"))

    # Etiqueta los conjuntos con las palabras
    venn.get_label_by_id('100').set_text('  Computación')
    venn.get_label_by_id('100').set_alpha(0.4)
    venn.get_label_by_id('101').set_text('Software\n tradicional')
    venn.get_label_by_id('110').set_text('Machine\n Learning')
    venn.get_label_by_id('010').set_text('Estadística')
    venn.get_label_by_id('010').set_alpha(0.4)
    venn.get_label_by_id('011').set_text(' Inv\n tradicional')
    venn.get_label_by_id('001').set_text('Dominio negocio')
    venn.get_label_by_id('001').set_alpha(0.4)
    venn.get_label_by_id('111').set_text('Ciencia\n de\n datos')

    # Ajusta el tamaño de fuente de las etiquetas
    for label in venn.set_labels:
        label.set_fontsize(12)
    for label in venn.subset_labels:
        label.set_fontsize(10)

    plt.figure(figsize=(10, 10))
    plt.show()
    st.pyplot(fig)


if __name__ == "__main__":
    main()




import { useState, useEffect } from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import { Container } from "react-bootstrap";
import axios from "axios";
import '../styles/Publication.css';
import toast, { Toaster } from 'react-hot-toast';

const CreatePublication = () => {
  const [Sendform, ChallengeSendForm] = useState(false);
  const [zones, setZones] = useState([]);
  const [publicationType, setPuplcationType] = useState([]);
  const initialValues = {
    title: "",
    description: "",
    phone: "",
    typeOfPublication: "",
    zone: "",
  };

  useEffect(()=>{
    const getSelects = async() =>{
      const zones = await axios.get('http://127.0.0.1:8000/api/zone')
      setZones(zones.data.zones);
      const type = await axios.get("http://127.0.0.1:8000/api/publicationtype")
      setPuplcationType(type.data.publicationType);

    }
    getSelects()
  },[]);
  


  const validateform = (values) => {
    let errors = {};
    if (!values.title) {
      errors.title = "Por favor, inserte el titulo de la publicacion";
    } else if (!/^[a-zA-ZÁ-ÿ0-9\s]{1,20}$/.test(values.title)) {
      errors.title = "El titulo solo puede contener letras, espacios y numeros (max 20 caracteres)";
    }

    if (!values.description) {
      errors.description = "Por favor ingrese una descripcion";
    } else if (!/^[a-zA-ZÁ-ÿ0-9\s]{1,100}$/.test(values.description)) {
      errors.description =
        "La descripcion solo puede contener letras, espacios y numeros";
    }
    if (!values.phone) {
      errors.phone = "Por favor inserte un numero de telefono";
    } else if (!/^[0-9]*$/.test(values.phone)) {
      errors.phone = "Este campo solo puede contener numeros sin espacios ni guiones";
    }else if(!/^\d{9,13}$/.test(values.phone)){
      errors.phone = "Digite un numero de telefono valido"
    }
    if (!values.typeOfPublication) {
      errors.typeOfPublication = "Por favor seleccione una Categoria";
    }
    if (!values.zone ) {
      errors.zone = "Por favor seleccione una zona";
    } 


    return errors;
  };
  const ApiConnection = async (initialValues) => {
    const formData = new FormData();
    const data = {
      "title": initialValues.title,
      "description": initialValues.description,
      "phone": initialValues.phone,
      "publication_type_id": initialValues.typeOfPublication,
      "user_id":"1",
      "zone_id": initialValues.zone
    }
    formData.append("files", data);
    await axios
      .post("http://127.0.0.1:8000/api/publication/", data)
      .then((response) => {
        return response
      })
      .catch((error) => {
        console.log(error);
      });
  };
  
  
  return (
    <Container>
      <div>
        <h1 className="title">Crear Publicacion</h1>
      </div>
      <Formik
        className="FormikStile"
        initialValues={initialValues}
        validate={validateform}
        onSubmit={(values, { resetForm }) => {
          console.log(values);
          resetForm();
          ChallengeSendForm(true);
          setTimeout(() => ChallengeSendForm(false), 5000);
          ApiConnection(values);
        }}
      >
        {({ errors }) => (
          <Form className="form">
            <div className="col-md-3">
              <label htmlFor="title">Titulo de la publicacion</label>
              <Field
                className="form-control"
                type="text"
                id="title"
                name="title"
                placeholder="Ingrese el titulo"
              />
              <ErrorMessage
                title="title"
                component={() => <div className="errors">{errors.title}</div>}
              />
            </div>
            
            <div className="col-md-3">
              <label htmlFor="description">Descripcion</label>
              <Field
                as="textarea"
                placeholder="Ingrese una descripcion"
                className="form-control"
                type="text"
                name="description"
              />
              <ErrorMessage
                name="description"
                component={() => (
                  <div className="errors">{errors.description}</div>
                )}
              />
            </div>

            <div className="col-md-3">
              <label htmlFor="phone">Telefono</label>
              <Field
                placeholder="Inserte el numero de telefono"
                className="form-control"
                type="numeric"
                name="phone"
              />
              <ErrorMessage
                name="phone"
                component={() => <div className="errors">{errors.phone}</div>}
              />
            </div>
            <div className="Type-of-Publication">
              <p htmlFor="typeOfPublication"> Categoria</p>
              <Field name="typeOfPublication" as="select">
                <option value=""></option>
                {publicationType.map(element=>(
                  <option key={element.id} value={element.id}>{element.description}</option>
                
                  ))
                }
              </Field>
              <ErrorMessage
                name="typeOfPublication"
                component={() => (
                  <div className="errors">{errors.typeOfPublication}</div>
                )}
              />
            </div>

            <div className="zone">
              <p htmlFor="zone"> Zona </p>
              <Field name="zone" as="select">
              <option value=""></option>
              {zones.map(element=>(
                <option key={element.id} value={element.id}>{element.description}</option>

                ))
              }
              </Field>
              <ErrorMessage
                name="zone"
                component={() => (
                  <div className="errors">{errors.zone}</div>
                )}
              />
            </div>


            <button type="submit">Publicar</button>

            {Sendform && (
              <p className="nice"> Publicacion creada exitosamente</p>
            )}
          </Form>
        )}
      </Formik>
    </Container>
  );
};

export default CreatePublication;

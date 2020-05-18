import React, { useState } from "react";
import { Grid, Header, Form, Button, Message } from "semantic-ui-react";
import { CountryDropdown } from "react-country-region-selector";
import regs from "../apis/regs";
import { Link, useHistory } from "react-router-dom";

const style = {
  title: {
    marginTop: "1em",
  },
};

const RegistrationForm = () => {
  let history = useHistory();
  const [country, setCountry] = useState("");
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState(null);

  const createNewUser = async () => {
    const formData = {
      first_name: fname,
      last_name: lname,
      email: email,
      country_code: country,
    };
    try {
      const response = await regs
        .post("/api/registrations/", formData)
        .then((response) => {
          if (response.status === 201) {
            setCountry("");
            setEmail("");
            setFname("");
            setLname("");
            setError("");
            history.push("/member-list");
          }
        })
        .catch((error) => {
          if (error.response.data?.email) {
            setError(error.response.data.email);
          } else {
            setError("There was an issue, please try again.");
          }
        });
    } catch (err) {
      setError(err);
    }
  };

  return (
    <>
      <Grid.Row>
        <Header as="h1" content="Register new user" style={style.title} />
      </Grid.Row>
      {error && (
        <Grid.Row>
          <Message floating negative>
            {error}
          </Message>
        </Grid.Row>
      )}
      <Grid.Row>
        <Form onSubmit={createNewUser}>
          <Form.Field>
            <label>First Name</label>
            <input
              placeholder="Joe"
              value={fname}
              onChange={(event) => setFname(event.target.value)}
            />
          </Form.Field>
          <Form.Field>
            <label>Last Name</label>
            <input
              placeholder="Blogs"
              value={lname}
              onChange={(event) => setLname(event.target.value)}
            />
          </Form.Field>
          <Form.Field>
            <label>Email</label>
            <input
              placeholder="valid@email.here"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
          </Form.Field>
          <Form.Field>
            <label>Country</label>
            <CountryDropdown
              value={country}
              onChange={(val) => setCountry(val)}
            />
          </Form.Field>
          <Button primary type="submit">
            Submit
          </Button>
        </Form>
      </Grid.Row>
      <Grid.Row>
        <Button secondary as={Link} to="/">
          Cancel
        </Button>
      </Grid.Row>
    </>
  );
};

export default RegistrationForm;

import React, { useEffect, useState } from "react";
import { Header, Grid, List, Button } from "semantic-ui-react";
import { Link } from "react-router-dom";
import regs from "../apis/regs";
import RegistrationListItem from "./RegistrationsListItem";

const style = {
  title: {
    marginTop: "1em",
  },
};
const RegistrationsList = () => {
  let listItems;
  const [members, setMembers] = useState([]);
  const getRegistrations = async () => {
    const response = await regs.get("/api/registrations/");

    if (response.data) {
      setMembers(response.data);
    }
  };

  useEffect(() => {
    getRegistrations();
  }, []);

  if (members) {
    listItems = members.map((member) => (
      <RegistrationListItem key={member.email} member={member} />
    ));
  }

  return (
    <>
      <Grid.Row>
        <Header as="h2" style={style.title}>
          Current Registrations
        </Header>
      </Grid.Row>
      <Grid.Row>
        <Button secondary as={Link} to="/">
          Go back home
        </Button>
      </Grid.Row>
      <Grid.Row columns={2}>
        <Grid.Column stretched>
          <List divided relaxed size="large">
            {listItems}
          </List>
        </Grid.Column>
      </Grid.Row>
    </>
  );
};

export default RegistrationsList;

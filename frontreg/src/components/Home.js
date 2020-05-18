import React from "react";
import {
  Grid,
  Header,
  Segment,
  Divider,
  Icon,
  Button,
} from "semantic-ui-react";
import { Link } from "react-router-dom";

const style = {
  title: {
    marginTop: "1em",
  },
  subtitle: {
    padding: "1em 0em",
  },
};

const Home = () => {
  return (
    <>
      <Grid.Row>
        <Grid.Column>
          <Header
            as="h1"
            content="reggie"
            style={style.title}
            textAlign="center"
          />
          <Header
            as="h5"
            content="The simple registration and 3rd party API integration tool"
            style={style.subtitle}
            textAlign="center"
          />
        </Grid.Column>
      </Grid.Row>
      <Grid.Row>
        <Grid.Column>
          <Grid.Row>
            <Segment placeholder>
              <Grid columns={2} stackable textAlign="center">
                <Divider vertical>Or</Divider>

                <Grid.Row verticalAlign="middle">
                  <Grid.Column>
                    <Header icon>
                      <Icon name="add user" />
                      New Registration
                    </Header>
                    <Button primary as={Link} to="/register">
                      Register
                    </Button>
                  </Grid.Column>
                  <Grid.Column>
                    <Header icon>
                      <Icon name="list" />
                      Registration List
                    </Header>

                    <Button secondary as={Link} to="/member-list">
                      Go to list
                    </Button>
                  </Grid.Column>
                </Grid.Row>
              </Grid>
            </Segment>
          </Grid.Row>
        </Grid.Column>
      </Grid.Row>
    </>
  );
};

export default Home;

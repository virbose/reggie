import React from "react";
import { Route, Switch } from "react-router-dom";
import { Grid } from "semantic-ui-react";
import Home from "./components/Home";
import RegistrationForm from "./components/RegistrationForm";
import RegistrationsList from "./components/RegistrationsList";

function App() {
  return (
    <Grid centered columns={2}>
      <Switch>
        <Route path="/register" exact>
          <RegistrationForm />
        </Route>
        <Route path="/member-list" exact>
          <RegistrationsList />
        </Route>
        <Route path="/" exact>
          <Home />
        </Route>
      </Switch>
    </Grid>
  );
}

export default App;

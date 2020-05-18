import React from "react";
import { List, Divider, Table, Segment, Header } from "semantic-ui-react";

const style = {
  listItem: {
    padding: "1em 0",
  },
  header: {
    marginTop: 10,
  },
};

const RegistrationListItem = ({ member }) => {
  const plans = member?.plans.map((plan) => (
    <Table.Row key={plan.name}>
      <Table.Cell>{plan.name}</Table.Cell>
      <Table.Cell>{plan.billing_interval}</Table.Cell>
      <Table.Cell>{plan.frequency}</Table.Cell>
      <Table.Cell>{plan.currency}</Table.Cell>
    </Table.Row>
  ));
  return (
    <Segment>
      <List.Item style={style.listItem}>
        <List.Icon name="user circle" size="big" verticalAlign="top" />
        <List.Content>
          <Header as="h3" style={style.header}>
            Member #{member.id}
          </Header>
          <Divider section />
          <List.Description>
            First Name: {member.first_name}
            <Divider />
            Last Name: {member.last_name}
            <Divider />
            Email: {member.email}
            <Divider />
            Country: {member.country_code}
            <Divider />
          </List.Description>
          <Table celled>
            <Table.Header>
              <Table.Row>
                <Table.HeaderCell>Plan Name</Table.HeaderCell>
                <Table.HeaderCell>Billing Interval </Table.HeaderCell>
                <Table.HeaderCell>Frequency</Table.HeaderCell>
                <Table.HeaderCell>Currency</Table.HeaderCell>
              </Table.Row>
            </Table.Header>
            <Table.Body>{plans}</Table.Body>
          </Table>
        </List.Content>
      </List.Item>
    </Segment>
  );
};

export default RegistrationListItem;

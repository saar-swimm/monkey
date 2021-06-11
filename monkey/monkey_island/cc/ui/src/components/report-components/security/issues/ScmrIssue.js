import React from 'react';
import CollapsibleWellComponent from '../CollapsibleWell';

export function scmrIssueOverview() {
    return (<li>Windows servers have RPC and SCMR ports open,
                      which leaves them vulnerable to remote service creation.</li>);
  }

export function scmrIssueReport(issue) {
    return (
      <>
        Block RPC and SCMR ports in the local firewall
        and secure the password of user {issue.username}.
        <CollapsibleWellComponent>
          The machine <span className="badge badge-primary">{issue.machine}</span> (<span
          className="badge badge-info" style={{margin: '2px'}}>{issue.ip_address}</span>) was
          exploited via <span className="badge badge-danger">MS-SCMR</span>.
          <br/>
          The attack was made possible because the target machine exposed RPC
          and SCMR ports and the Monkey was
          able to use {issue.username} credentials.
        </CollapsibleWellComponent>
      </>
    );
  }

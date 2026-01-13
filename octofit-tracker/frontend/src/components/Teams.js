import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched Teams:', results);
      });
  }, []);

  return (
    <div>
      <h2 className="mb-4 text-primary">Teams</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Name</th>
                <th>Members</th>
              </tr>
            </thead>
            <tbody>
              {teams.map((team, idx) => (
                <tr key={team.id || idx}>
                  <td>{team.name}</td>
                  <td>{Array.isArray(team.members) ? team.members.join(', ') : team.members}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <button className="btn btn-primary mt-3">Add Team</button>
        </div>
      </div>
    </div>
  );
}

export default Teams;

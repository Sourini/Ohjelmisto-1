const participant_list = [];

for (let i = 0; i < 6; i++) {participant_list.push(prompt('Enter the name of the dog: '))}

participant_list.sort().reverse();

const ordered_list = document.createElement('ul');

for (let i = 0; i < participant_list.length; i++) {
    const listed_participant = document.createElement('li');
    listed_participant.textContent = participant_list[i];
    ordered_list.appendChild(listed_participant);
}

document.body.appendChild(ordered_list)
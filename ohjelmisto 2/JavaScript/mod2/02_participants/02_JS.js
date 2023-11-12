the_amount = parseInt(prompt('Enter a number of participants: '))

let participant_list = [];

for (let i = 0; i < the_amount; i++) {participant_list.push(prompt('Enter the name of the participant: '))}

participant_list.sort();

const ordered_list = document.createElement('ol');

for (let i = 0; i < participant_list.length; i++) {
    const listed_participant = document.createElement('li');
    listed_participant.textContent = participant_list[i];
    ordered_list.appendChild(listed_participant);
}

document.body.appendChild(ordered_list)
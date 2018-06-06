import { Firebase, FirebaseRef } from '../lib/firebase';

export function getMemories() {
  if (Firebase === null) return () => new Promise(resolve => resolve());

  return dispatch => new Promise(resolve => FirebaseRef.child('memories')
    .on('value', (snapshot) => {
      const memories = snapshot.val() || {};

      return resolve(dispatch({
        type: 'MEMORIES_REPLACE',
        data: memories,
      }));
    })).catch(e => console.log(e));
}

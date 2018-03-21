import decode from 'jwt-decode'
import router from '../router'
import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5000'

export function register(username, password) {
  const url = `${BASE_URL}/register`
  return axios.post(url, {
    'username': username,
    'password': password
  }).then((response) => {
    console.log(response.data['message'])
    alert(`User ${username}`)
    router.go('/')
  })
}

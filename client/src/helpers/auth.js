import decode from 'jwt-decode'
import router from '../router'
import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5000'
const TOKEN = 'token'

function getToken () {
  return localStorage.getItem(TOKEN)
}

export function register (username, password) {
  const url = `${BASE_URL}/register`
  return axios.post(url, {
    'username': username,
    'password': password
  }).then((response) => {
    console.log(response.data['message'])
    alert(`User ${username}`)
    router.push('/login')
  })
}

export function testroute () {
  router.push('/')
}

export function login (username, password) {
  const url = `${BASE_URL}/login`
  return axios.post(url, {
    'username': username,
    'password': password
  }).then((response) => {
    localStorage.setItem(TOKEN, response.data['token'])
    router.push('/')
  })
}

export function logout () {
  localStorage.removeItem(TOKEN)
  router.push('/')
}

export function isLoggedIn () {
  const token = getToken()
  return !!token && !isTokenExpired(token)
}

function getTokenExpirationDate (encodedToken) {
  const token = decode(encodedToken)
  if (!token.exp) { return null }

  const date = new Date(0)
  date.setUTCSeconds(token.exp)

  return date
}

function isTokenExpired (token) {
  const expirationDate = getTokenExpirationDate(token)
  return expirationDate < new Date()
}

import axios from "axios"

export const handleTokenRefresh = async () => {
    try {
      const refreshResponse = await axios.post(
        'http://127.0.0.1:5000/refresh',
        {},
        {
          headers: { Authorization: `Bearer ${localStorage.getItem('refresh_token')}` }
        }
      )
      const newAccessToken = refreshResponse.data.access_token
      sessionStorage.setItem('access_token', newAccessToken)
      return newAccessToken
    } catch (error) {
      console.error('Failed to refresh token:', error)
      alert('Session expired. Please log in again.')
      // Redirect to login
      window.location.href = '/'
      return null
    }
  }
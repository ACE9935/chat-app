import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';
import AuthPage from './components/pages/AuthPage';
import ChatPage from './components/pages/ChatPage';
import ChatRoom from './components/pages/ChatRoom'; // your new chat room component
import { UserProvider } from './components/context/UserContext';
import { PrivateRoute } from './components/context/PrivateRoute';
import HomePage from './components/pages/HomePage';

function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage/>} />
          <Route path="/auth" element={<AuthPage />} />
          <Route path="/chat" element={<PrivateRoute><ChatPage /></PrivateRoute>} />
          {/* Dynamic room route */}
          <Route path="/chat/:roomId" element={<PrivateRoute><ChatRoom /></PrivateRoute>} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;

import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';
import AuthPage from './components/pages/AuthPage';
import ChatPage from './components/pages/ChatPage';
import ChatRoom from './components/pages/ChatRoom'; // your new chat room component
import { UserProvider } from './components/context/UserContext';

function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path="/auth" element={<AuthPage />} />
          <Route path="/chat" element={<ChatPage />} />
          {/* Dynamic room route */}
          <Route path="/chat/:roomId" element={<ChatRoom />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;

# Patentability Detector

## Overview

The Patentability Detector is a web application that analyzes GitHub repositories to identify potentially patentable software components. The system automatically evaluates code files to distinguish between novel, patentable innovations and standard, non-patentable implementations. It provides detailed analysis reports with patentability scores, risk assessments, and rationale for each identified component.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Full-Stack Architecture
The application follows a monorepo structure with separate client and server directories, sharing common types and schemas through a shared module. The architecture supports both development and production environments with proper build processes.

### Frontend (React + TypeScript)
- **Framework**: React 18 with TypeScript for type safety
- **Routing**: Wouter for lightweight client-side routing
- **State Management**: TanStack Query for server state management and caching
- **UI Framework**: shadcn/ui components built on Radix UI primitives
- **Styling**: Tailwind CSS with CSS variables for theming
- **Forms**: React Hook Form with Zod validation for type-safe form handling
- **Build Tool**: Vite for fast development and optimized production builds

### Backend (Express + TypeScript)
- **Framework**: Express.js server with TypeScript
- **Runtime**: Node.js with ESM modules
- **API Design**: RESTful endpoints with WebSocket support for real-time progress updates
- **File Processing**: Direct GitHub API integration for repository analysis
- **Session Management**: Express sessions with PostgreSQL storage
- **Error Handling**: Centralized error middleware with proper HTTP status codes

### Database Layer
- **ORM**: Drizzle ORM for type-safe database operations
- **Database**: PostgreSQL with Neon serverless hosting
- **Schema Management**: Drizzle Kit for migrations and schema evolution
- **Storage Pattern**: Repository and Component entities with relationship mapping

### AI Integration
- **Service**: OpenAI GPT integration for code analysis and component evaluation
- **Analysis Pipeline**: Multi-step process analyzing file contents, component types, and patentability factors
- **Scoring System**: Numerical scoring for novelty, utility, and prior art risk assessment

### Real-time Communication
- **WebSockets**: Live progress updates during repository analysis
- **Progress Tracking**: Step-by-step analysis progress with detailed status messages
- **Connection Management**: Automatic reconnection and error handling

### Development Workflow
- **Build System**: Separate client and server build processes with shared type definitions
- **Development Server**: Hot module replacement with Vite middleware integration
- **Production Deployment**: Bundled server with static client assets
- **Code Quality**: TypeScript strict mode with comprehensive type checking

## External Dependencies

### Cloud Services
- **Neon Database**: Serverless PostgreSQL hosting for production data storage
- **OpenAI API**: GPT models for intelligent code analysis and component evaluation
- **GitHub API**: Repository content access and metadata retrieval
- **Replit Platform**: Development environment with connector integrations

### Third-Party Libraries
- **UI Components**: Radix UI primitives for accessible, unstyled component foundations
- **Styling**: Tailwind CSS for utility-first styling with shadcn/ui design system
- **Data Fetching**: TanStack Query for server state management and optimistic updates
- **Form Handling**: React Hook Form with Hookform Resolvers for validation integration
- **Validation**: Zod for runtime type validation and schema definition
- **Date Utilities**: date-fns for date manipulation and formatting
- **Code Highlighting**: Potential integration for syntax highlighting in code previews

### Development Tools
- **Build Tools**: Vite for frontend bundling, esbuild for server compilation
- **Type System**: TypeScript with strict configuration and path mapping
- **Database Tools**: Drizzle Kit for schema management and migrations
- **Replit Integrations**: Development plugins for enhanced Replit IDE experience
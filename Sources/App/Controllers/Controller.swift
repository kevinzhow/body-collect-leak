import Vapor

struct Controller: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        routes.grouped("file").on(.POST, "upload", body: .collect(maxSize: "30mb"), use: create)
    }
    
     func create(req: Request) async throws -> HTTPStatus {
        return .ok
     }
}